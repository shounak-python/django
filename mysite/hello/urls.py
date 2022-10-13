from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.myview),
    path('owner', views.owner, name='owner'),]