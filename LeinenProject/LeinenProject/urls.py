"""LeinenProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import app.views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app.views.home_handler,name='inicio'),
    path('home/',app.views.home_handler,name='home'),
    path('about/',app.views.about_handler,name='about'),
    path('contacto/',app.views.contacto_handler,name='contacto'),
    path('cv/',app.views.cv_handler,name='cv'),
    path('portfolio/',app.views.portfolio_handler,name='portfolio'),
    path('gallery/<str:id>',app.views.album_handler,name='gallery')

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)