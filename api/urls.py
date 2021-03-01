
from django.urls import include, path
from api.views import RoomView

urlpatterns = [
    path('', RoomView.as_view(), name='room_view')
]