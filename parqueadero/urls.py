from django.contrib import admin
from django.urls import path
from parqueadero import views

urlpatterns = [
    path('',views.first_view,name='base'),
    path('propietario',views.propietario,name='propietario-list'),
    path('propietario/<int:propietario_id>/detail/', views.propietario_detail, name='propietario-detail'),
    
    path('vehiculo/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculo/<int:pk>/detail/', views.VehiculoDetailView.as_view(), name='vehiculo-detail'),
     # Update
    path('vehiculo/<int:pk>/update/', views.VehiculoUpdate.as_view(), name='vehiculo-update'),
    #Create
    path('vehiculo/create/', views.VehiculoCreate.as_view(), name='vehiculo-create'),
    #Delete
    path('vehiculo/<int:pk>/delete/', views.VehiculoDelete.as_view(), name='vehiculo-delete'),
    # Update
    path('propietario/<int:pk>/update/', views.PropietarioUpdate.as_view(), name='propietario-update'),
    #Create
    path('propietario/create/', views.PropietarioCreate.as_view(), name='propietario-create'),
    #Delete
    path('propietario/<int:pk>/delete/', views.PropietarioDelete.as_view(), name='propietario-delete'),
    
    ]