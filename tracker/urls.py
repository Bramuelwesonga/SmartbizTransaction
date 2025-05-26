# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),  # If you have export implemented
]
