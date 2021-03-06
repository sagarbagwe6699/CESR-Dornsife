from calendar import week
from pyexpat import model
from re import template
from statistics import mode
from threading import Thread
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ChatMessage, Thread
from django.http import HttpResponse, HttpResponseRedirect
import json
from datetime import date
import re

# Create your views here.


class HomeView(ListView):
    model = Thread
    template_name = 'home.html'
    # extra_context = {'user_id': }

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['user_id'] = self.request.GET.get('user')
        return context

    # def get_queryset(self):
    #     self.user_id = self.request.GET.get('user')
    #     qs = super().get_queryset()
    #     return qs

    # def get(self, request, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     print(context['request'].GET.get('user'))
    #     context['user_id'] = context['request'].GET.get('user')
    #     return self.render_to_response(context)


class DiscussionDetail(DetailView):
    model = Thread
    template_name = 'discussion_detail.html'


def DetailDiscussion(request, primary_key=None, user_id=None):
    mappings = {"39cb93-8411cd-b2381b-e3aaa4-b9d710": "Gema",
                "777ec0-4c1213-877b87-35d594-15e5ea": "Jose",
                "88aacd-618237-45de4d-dcc784-a74ce9": "Maria P.",
                "d96ce3-378a38-947f4b-f0554c-a97d4a": "Avril",
                "3e3e5e-42e9d8-49dc10-9dfe50-2fdca1": "Juan",
                "5055ad-e0aa26-3e499a-964d81-80e4f8": "Jorge",
                "5055ad-e0aa26-3e499a-964d81-80e4gg": "Luisa B.",
                "5055ad-e0aa26-3e499a-964d81-80e4ss": "Patricia D."
                }
    res = Thread.objects.get(primary_key=primary_key)
    topic = res.topic
    link_text = res.inforgraphic_text
    link = res.infographic_link
    # res = json.loads(res.messages.replace("\'", "\""))
    author = mappings[user_id]
    m = ChatMessage.objects.filter(week=res.week)

    if request.method == 'POST':
        text = request.POST.get('chat-message', '')
        if text != '':
            m = ChatMessage()
            r = re.compile(r"(https://[^ ]+)")
            print(r.sub(r'<a href="\1">\1</a>', text))
            m.message = r.sub(r'<a href="\1">\1</a>', text)
            m.week = res.week
            m.author = author if author else 'Untitled'
            m.time_stamp = date.today()
            m.save()
            return HttpResponseRedirect('{}'.format(user_id))
        # text = request.POST.get('chat-message', '')
        # res.append({"message": text, "author": author,
        #            "timestamp": date.today().strftime("%B %d, %Y")})
        # if text != '':
        #     Thread.objects.filter(id=pk).update(messages=res)
        #     return HttpResponseRedirect('{}'.format(user_id))

    return render(request, 'discussion_detail.html', {"messages": m, "author": author, "user_id": user_id, "topic": topic, "link_text": link_text, "link": link})
