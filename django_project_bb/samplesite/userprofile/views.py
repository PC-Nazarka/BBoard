from django.views import generic
from django.contrib.auth.models import User
from bboard import models
from .forms import UserChangeForm
from chat.models import Room


class ProfileView(generic.ListView):
    template_name = 'userprofile/profile.html'
    context_object_name = 'current_item'

    def get_queryset(self):
        user_item = User.objects.get(pk=self.kwargs['pk'])
        object_list = models.Bb.objects.filter(user=user_item)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_bb'] = models.Bb.objects.all()
        context['current_user'] = User.objects.get(pk=self.kwargs['pk'])
        if self.request.user != context["current_user"]:
            room = None
            if Room.objects.filter(member_first=self.request.user).filter(member_second=context['current_user']):
                room = Room.objects.filter(member_first=self.request.user).filter(member_second=context['current_user'])
            elif Room.objects.filter(member_second=self.request.user).filter(member_first=context['current_user']):
                room = Room.objects.filter(member_second=self.request.user).filter(member_first=context['current_user'])
            else:
                if context['current_user'] != self.request.user:
                    room = Room.objects.create(member_first=context['current_user'], member_second=self.request.user)
            room = room[0]

            context['room'] = room.id
        return context


class UpdateUserProfile(generic.UpdateView):
    template_name = 'userprofile/update_profile.html'
    model = User
    form_class = UserChangeForm
    success_url = '/'
