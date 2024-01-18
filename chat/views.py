from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Message, ChatRoom
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    chat_rooms = ChatRoom.objects.all()
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'home.html', {'chat_rooms': chat_rooms, 'users': users})

@login_required
def chat_room(request, chat_room_id):
    chat_room = ChatRoom.objects.get(id=chat_room_id)
    if request.method == 'POST':
        text = request.POST['text']
        Message.objects.create(chat_room=chat_room, user=request.user, text=text)
        return redirect('chat_room', chat_room_id=chat_room.id)  # Redirect back to the chat room
    return render(request, 'chat_room.html', {'chat_room': chat_room})

@login_required
def start_chat(request, user_id):
    # Get the other user
    other_user = User.objects.get(id=user_id)

    # Create a new chat room with just the two users
    chat_room = ChatRoom.objects.create()
    chat_room.users.add(request.user, other_user)

    # Redirect the user to the new chat room
    return redirect('chat_room', chat_room_id=chat_room.id)
