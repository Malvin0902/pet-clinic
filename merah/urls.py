from django.urls import path, re_path
from merah import views

app_name = 'merah'

urlpatterns = [
    path('vaksinasi/', views.list_vaksinasi, name='list_vaksinasi'), 
    path('vaksinasi/add/', views.add_vaksinasi, name='add_vaksinasi'), 
    path('vaksinasi/update/<uuid:id_kunjungan>/', views.update_vaksinasi, name='update_vaksinasi'), 
    path('vaksinasi/delete/<uuid:id_kunjungan>/', views.delete_vaksinasi, name='delete_vaksinasi'),
    path('vaksin/', views.list_vaksin, name='list_vaksin'),
    path('vaksin/add/', views.add_vaksin, name='add_vaksin'),
    path('vaksin/update/<str:kode_vaksin>/', views.update_vaksin, name='update_vaksin'),
    path('vaksin/update-stok/<str:kode_vaksin>/', views.update_stok_vaksin, name='update_stok_vaksin'),
    path('vaksin/delete/<str:kode_vaksin>/', views.delete_vaksin, name='delete_vaksin'),
    path('klien/', views.list_klien, name='list_klien'),
    path('klien/<uuid:client_id>/', views.detail_klien, name='detail_klien'),
    path('list-vaksinasi-hewan/', views.list_vaksin_hewan, name='list_vaksin_hewan'),

]
