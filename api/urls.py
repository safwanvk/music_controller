
from django.urls import include, path
from api.views import hello

urlpatterns = [

    path('', hello)
]