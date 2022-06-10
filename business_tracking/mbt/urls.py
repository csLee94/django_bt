from django.urls import path

from . import views 

app_name = "mbt"

urlpatterns = [
    path('inbound/',views.inbound, name="inbound"),
    path('inbound/<int:inbound_id>/', views.inbound_detail, name='inbound_detail'),
    path('inbound/transfer/<int:inbound_id>', views.inbound_to_contract, name="inbound_to_contract"),
    path('inbound/addact/<int:inbound_id>', views.add_inbound_history, name="add_inbound_action"),
    path('inbound/create/', views.create_inbound, name='create_inbound'),
    path('contract/', views.contract, name='contract'),
    path('contract/<int:contract_id>/', views.contract_detail, name='contract_detail'),
    path('contract/create/', views.create_contract, name='create_contract'),
    path('contract/addproduct/<int:contract_id>/', views.add_product, name='add_product'),
    path('contract/addbillingrev/<int:contract_id>/', views.add_billing_revenue, name='add_billing_revenue'),
]