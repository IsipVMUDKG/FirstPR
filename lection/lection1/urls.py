from django.urls import path
from . import views

urlpatterns = [

    path('clienti/', views.ClientiListView.as_view(), name='clienti_list'),
    path('clienti/<int:pk>/', views.ClientiDetailView.as_view(), name='clienti_detail'),
    path('clienti/create/', views.ClientiCreateView.as_view(), name='clienti_create'),
    path('clienti/<int:pk>/update/', views.ClientiUpdateView.as_view(), name='clienti_update'),
    path('clienti/<int:pk>/delete/', views.ClientiDeleteView.as_view(), name='clienti_delete'),
    
    path('mendgeri/', views.MendgeriListView.as_view(), name='mendgeri_list'),
    path('mendgeri/<int:pk>/', views.MendgeriDetailView.as_view(), name='mendgeri_detail'),
    path('mendgeri/create/', views.MendgeriCreateView.as_view(), name='mendgeri_create'),
    path('mendgeri/<int:pk>/update/', views.MendgeriUpdateView.as_view(), name='mendgeri_update'),
    path('mendgeri/<int:pk>/delete/', views.MendgeriDeleteView.as_view(), name='mendgeri_delete'),
    
    path('tarif/', views.Tarifini_planListView.as_view(), name='tarif_list'),
    path('tarif/<int:pk>/', views.Tarifini_planDetailView.as_view(), name='tarif_detail'),
    path('tarif/create/', views.Tarifini_planCreateView.as_view(), name='tarif_create'),
    path('tarif/<int:pk>/update/', views.Tarifini_planUpdateView.as_view(), name='tarif_update'),
    path('tarif/<int:pk>/delete/', views.Tarifini_planDeleteView.as_view(), name='tarif_delete'),

    path('podchenie/', views.Podchenie_nomeraListView.as_view(), name='podchenie_list'),
    path('podchenie/<int:pk>/', views.Podchenie_nomeraDetailView.as_view(), name='podchenie_detail'),
    path('podchenie/create/', views.Podchenie_nomeraCreateView.as_view(), name='podchenie_create'),
    path('podchenie/<int:pk>/update/', views.Podchenie_nomeraUpdateView.as_view(), name='podchenie_update'),
    path('podchenie/<int:pk>/delete/', views.Podchenie_nomeraDeleteView.as_view(), name='podchenie_delete'),

    path('jurnal/', views.JurnalListView.as_view(), name='jurnal_list'),
    path('jurnal/<int:pk>/', views.JurnalDetailView.as_view(), name='jurnal_detail'),
    path('jurnal/create/', views.JurnalCreateView.as_view(), name='jurnal_create'),
    path('jurnal/<int:pk>/update/', views.JurnalUpdateView.as_view(), name='jurnal_update'),
    path('jurnal/<int:pk>/delete/', views.JurnalDeleteView.as_view(), name='jurnal_delete')
]