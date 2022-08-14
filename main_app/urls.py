from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('location/', views.LocationList.as_view(), name='location_index'),
    path('location/create/', views.LocationCreate.as_view(), name='location_create'),
    path('location/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
    path('location/<int:pk>/update', views.LocationUpdate.as_view(), name='location_update'),
    path('location/<int:pk>/delete', views.LocationDelete.as_view(), name='location_delete'),
]