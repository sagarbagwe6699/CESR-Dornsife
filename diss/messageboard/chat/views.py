from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import usermessage
from datetime import date

# Create your views here.


def discussions(request):
    mappings = {"39cb93-8411cd-b2381b-e3aaa4-b9d710": "Gema",
                "777ec0-4c1213-877b87-35d594-15e5ea": "Jose",
                "88aacd-618237-45de4d-dcc784-a74ce9": "Maria P.",
                "d96ce3-378a38-947f4b-f0554c-a97d4a": "Avril",
                "3e3e5e-42e9d8-49dc10-9dfe50-2fdca1": "Juan",
                "5055ad-e0aa26-3e499a-964d81-80e4f8": "Jorge",
                "5055ad-e0aa26-3e499a-964d81-80e4f8": "Luisa B.",
                "5055ad-e0aa26-3e499a-964d81-80e4f8": "Patricia D."
                }
    messages = usermessage.objects.all()
    id_ = request.GET.get('user')
    author = ''
    if id_:
        author = mappings[id_]
    if request.method == 'POST':
        text = request.POST.get('chat-message', '')
        if text != '':
            m = usermessage()
            m.text = text
            m.author = author if author else 'Untitled'
            m.time = date.today()
            m.save()
            return HttpResponseRedirect('?user={}'.format(id_))
    return render(request, 'index.html', {'messages': messages, 'author': author})
