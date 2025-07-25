from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('members/', views.members_list, name='members_list'),
    ]