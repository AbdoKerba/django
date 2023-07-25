from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Room, Message
from .forms import MessageForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    user = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return render(request, 'room.html', {
        'username': user,
        'room': room,
        'room_details': room_details,
        'messages': messages
    })

def checkview(request):
    room = request.POST['room']
    username = request.POST['user']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    print(request)
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    message_create = Message.objects.create(text=message, user=username, room=room_id)
    message_create.save()
    return HttpResponse("Message Added Successfully")

def getmessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})

class TestApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Message.objects.all()
        serialzer = MessageSerializer(qs, many=True)
        return Response(serialzer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)