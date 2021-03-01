
from django.urls import include, path
from api.views import RoomView, CreateRoomView

urlpatterns = [
    path('', RoomView.as_view(), name='room_view'),
    path('create-room', CreateRoomView.as_view(), name='create_room')
]