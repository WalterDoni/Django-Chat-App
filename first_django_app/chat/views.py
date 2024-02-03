from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Message,Chat
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')

def index(request):
 if request.method == 'POST':
     print('received data' + request.POST['textmessage'])
     myChat = Chat.objects.get(id=1)
     Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
 chatMessages = Message.objects.filter(chat__id=1)
 return render(request, 'chat/index.html',  {"messages" : chatMessages})

def logout_view(request):
  logout(request)
  return render(request, 'login/login.html')


def login_view(request):
   redirect = request.GET.get('next')
   if request.method == 'POST':
      user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
      if user: 
         login(request, user)
         return HttpResponseRedirect(request.POST.get('redirect'))
      else:
         return render(request,'login/login.html', {'wrongPassword': True, 'redirect':redirect })   
   return render(request,'login/login.html', {'redirect':redirect })


def register_view(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      if get_user_model().objects.filter(username=username).exists():
        return render(request, 'register/register.html', {'userExistAllready' : True})
      else:     
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )   
    return render(request, 'register/register.html')
