"""
URL configuration for bd_course project.

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

from authentication.views import ProfileUpdateView, ProfileDetailView, UserRegisterView, \
    UserLogoutView, UserLoginView, profiles_list
from club_members.views import index, map_view, locations_list, news_list, news_detail, \
    documents_list, upload_document, download_document, export_news_json, export_news_xml

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name="home"),
    path('about/', index, name="about"),

    path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('buy_crayfish/map/<int:location_id>/', map_view, name='buy_crayfish_map'),
    path('locations/', locations_list, name='locations_list'),
    path('profiles_list', profiles_list, name="profiles_list"),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('documents/', documents_list, name='documents_list'),
    path('upload/', upload_document, name='upload_document'),
    path('documents/download/<slug:slug>/', download_document, name='download_document'),

    path('news/export/json/', export_news_json, name='export_news_json'),
    path('news/export/xml/', export_news_xml, name='export_news_xml'),
]
