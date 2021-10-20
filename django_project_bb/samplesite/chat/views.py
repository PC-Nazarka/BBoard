from django.views import generic
from . import models
from django.db.models import Q


class HomeChat(generic.ListView):
    template_name = 'chat/list_chat.html'
    context_object_name = 'chat_item'

    def get_queryset(self):
        object_list = models.Room.objects.filter(Q(member_first=self.request.user) | Q(member_second=self.request.user))
        return object_list


class RoomChat(generic.TemplateView):
    template_name = 'chat/room.html'
    queryset = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = models.Room.objects.get(pk=self.kwargs['pk'])
        context['room_name'] = self.kwargs['pk']
        context['second_member'] = room.member_first if room.member_first.id != self.request.user.id else room.member_second
        context['username'] = self.request.user.username
        context['messages'] = models.Message.objects.filter(room=room)
        return context

