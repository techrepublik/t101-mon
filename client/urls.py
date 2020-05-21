from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('',  views.list_client, name='clients'),
    path('new/', views.new_client, name='new_client'),
    path('create/', views.create_client, name='create_client'),
    path('<int:pk>/update/', views.edit_client, name='edit_client'),
    path('<int:pk>/delete/', views.delete_client, name='delete_client'),
    path('report/', views.client_pdf, name='client_pdf'),
    path('monitor/', views.monitor_client, name='monitor_client'),
    path('monitor/<str:client>/', views.monitor_ping, name='monitor_ping'),
    path('monitor/create/<str:client>/', views.create_status, name='create_status'),
    path('status/', views.status_list, name='statuses'),
    path('status/create/', views.create_status1, name='create_status_1'),
    path('status/<int:pk>/update/', views.update_status, name='update_status'),
    path('status/<int:pk>/delete/', views.delete_status, name='delete_status'),
]
