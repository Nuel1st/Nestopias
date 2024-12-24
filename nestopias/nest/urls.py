from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('agent', views.agent, name='agent'),
    path('properties', views.properties, name='properties'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    # path('contact', views.contact, name='contact'),
]