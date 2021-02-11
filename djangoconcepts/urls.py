"""djangoconcepts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from fbv.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', add_or_update,name='first'),
    path('edit/<int:eid>', edit,name='update'),
    path('delete/<int:eid>', delete,name='delete'),
    path('adr/first/', add_or_update_address,name='first'),
    path('adr/edit/<int:aid>', edit_address,name='update'),
    path('adr/delete/<int:aid>', delete_adr,name='delete'),
]
