from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatUser, ChatMessage
from .forms import ChatMessageForm
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm #username, password
from django.contrib.auth import login, authenticate, logout


@login_required
def chat(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')[:50]
    form = ChatMessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.user = request.user
        message.save()
        return redirect('chat')
    return render(request, 'chat.html', {'messages': messages, 'form': form})

def homePage(request):
    return render(request, "index.html")

def signUpPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
    else:
        form = NewUserForm()

    return render(request, "sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("chat")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect("loginPage")