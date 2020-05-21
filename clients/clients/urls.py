"""clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from client import views

urlpatterns = [
    # path('clients/', client_views.list_client, name='clients'),
    # path('clients/new/', client_views.new_client, name='new_client'),
    # path('clients/<int:id>/update/', client_views.edit_client, name='update_client'),
    path('', views.list_client, name='list-client'),
    path('clients/', include('client.urls', namespace='client')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
