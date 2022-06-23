from django.urls import path
#from django.conf.urls import url
from intro_program import views

urlpatterns = [
    path('', views.index),
    #url(r'', views.default_map, name="default"),
    path('pdu/', views.intro_pdu, name='intro_pdu'),
    path('usc/', views.intro_usc, name='intro_usc'),
]