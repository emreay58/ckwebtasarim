from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('hizmetler/', views.ServicesView, name='services'),
    path('hizmetler/<slug:slug>', views.Services_Detail, name='services_detail'),
    path('hakkimizda/', views.AboutView, name="about"),
    path('fiyatlama/', views.PricingView, name="pricing"),
    path('referanslar/', views.ReferansView, name="referans"),
    path('teklif-formu/', views.TeklifView, name="teklif"),
    path('iletisim/', views.ContactView, name='contact'),
    ]
