
from django.urls import include, path
from api.views import RoomView, CreateRoomView, GetRoom, JoinRoom

urlpatterns = [
    path('', RoomView.as_view(), name='room_view'),
    path('create-room', CreateRoomView.as_view(), name='create_room'),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view())
]