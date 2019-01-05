from django.urls import path
from . import views

urlpatterns = [
    path('outbound/<int:id>/send', views.outbound_send, name='contacts-outbound-send'),
]