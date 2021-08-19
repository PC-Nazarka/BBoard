from django.urls import reverse_lazy
from django.views import generic
from . import forms
from . import models
from chat.models import Room
from django.db.models import Q

class MainPage(generic.list.ListView):
    model = models.Bb
    template_name = 'bboard/index.html'
    context_object_name = 'bbs'
    paginate_by = 5

    def get_queryset(self):
        return models.Bb.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = models.Rubric.objects.all()
        return context

class RenderByRubric(generic.list.ListView):
    model = models.Bb
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'
    paginate_by = 5

    def get_queryset(self):
        return models.Bb.objects.filter(rubric = self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = models.Rubric.objects.all()
        context['current_rubric'] = models.Rubric.objects.get(pk = self.kwargs['rubric_id'])
        return context
        
class CreateItem(generic.CreateView):
    model = models.Bb
    success_url = '/'
    template_name = 'bboard/create.html'
    form_class = forms.BbForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NewItemPage(generic.DetailView, generic.edit.FormMixin):
    model = models.Bb
    template_name = 'bboard/cart_item.html'
    context_object_name = 'item_bb'
    form_class = forms.CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = models.Bb.objects.get(pk=self.kwargs['pk']).user
        if Room.objects.filter(member_first = self.request.user).filter(member_second = member):
            room = Room.objects.filter(member_first = self.request.user).filter(member_second = member)
        elif Room.objects.filter(member_second = self.request.user).filter(member_first = member):
            room = Room.objects.filter(member_second = self.request.user).filter(member_first = member)
        else:
            room = Room.objects.create(member_first = member, member_second = self.request.user)
        room = room[0]
        context['room'] = room.id
        return context

    def get_success_url(self):
        return reverse_lazy('bboard:page', kwargs={'pk':self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.bboard = self.get_object()
        form.instance.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ItemUpdate(generic.UpdateView):
    model = models.Bb
    template_name = 'bboard/create.html'
    form_class = forms.BbForm

class ItemDelete(generic.DeleteView):
    model = models.Bb
    success_url = '/'
    context_object_name = 'item_bb'
    form_class = forms.BbForm

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SearchResults(generic.ListView):
    model = models.Bb
    template_name = 'bboard/search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = models.Bb.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) 
            | Q(title__icontains=query.upper()) | Q(content__icontains=query.upper())
            | Q(title__icontains=query.lower()) | Q(content__icontains=query.lower())
            | Q(title__icontains=query.capitalize()) | Q(content__icontains=query.capitalize()))
        else:
            object_list = None

        return object_list
