from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', admin.site.urls),
    path('general/', views.v_general),
    path('out/', views.v_out),
    path('general_main/', views.v_general_main),
    path('general_search/', views.v_general_search),
    path('out_search/', views.v_out_search),
    path('about/', views.about),
]
