"""
URL configuration for Hospital_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hospital_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login_admin,name="login"),
    path('logout/',views.logout_admin,name="logout"),
    path('index/',views.index,name="index"),
    path('viewdoc/',views.view_doctor,name="viewdoc"),
    path('adddoc/',views.add_doctor,name="adddoc"),
    path('deletedoc(?P<int:pid>)/',views.delete_doctor,name="deletedoc"),
    path('viewper/',views.view_patient,name="viewper"),
    path('addper/',views.add_patient,name="addper"),
    path('deleteper(?P<int:pid>)/',views.delete_patient,name="deleteper"),

    path('viewapin/',views.view_appointment,name="viewapin"),
    path('addapin/',views.add_appointment,name="addapin"),
    path('deleteapin(?P<int:pid>)/',views.delete_appointment,name="deleteapin"),
    
]
