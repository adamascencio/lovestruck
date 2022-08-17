from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('locations/', views.LocationList.as_view(), name='location_index'),
    path('locations/create/', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
    path('locations/<int:pk>/update', views.LocationUpdate.as_view(), name='location_update'),
    path('locations/<int:pk>/delete', views.LocationDelete.as_view(), name='location_delete'),
    path('partners/', views.PartnerList.as_view(), name='partner_index'),
    path('partners/create/', views.PartnerCreate.as_view(), name='partner_create'),
    path('partners/<int:pk>/', views.PartnerDetail.as_view(), name='partner_detail'),
    path('partners/<int:pk>/update', views.PartnerUpdate.as_view(), name='partner_update'),
    path('partners/<int:pk>/delete', views.PartnerDelete.as_view(), name='partner_delete'),
    path('dates/', views.DateList.as_view(), name='date_index'),
    path('dates/create/', views.DateCreate.as_view(), name='date_create'),
    path('dates/<int:pk>/', views.DateDetail.as_view(), name='date_detail'),
]