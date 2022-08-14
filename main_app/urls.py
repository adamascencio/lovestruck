from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('location/', views.LocationList.as_view(), name='location_index'),
    path('location/create/', views.LocationCreate.as_view(), name='location_create'),
    path('accounts/signup/', views.signup, name='signup'),
]