from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact_form, name='contact'),
    path('contacts/', views.contact_list, name='contact_list'),
]