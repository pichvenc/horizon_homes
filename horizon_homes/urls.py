"""
URL configuration for horizon_homes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from horizon_homes import settings
from horizon_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('properties', views.properties, name='properties'),
    path('property/<uuid:property_id>', views.single_property, name='single_property'),
    path('book_viewing/<uuid:property_id>', views.book_viewing, name='book_viewing'),
    path('page-not-found', views.page_not_found, name='404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
