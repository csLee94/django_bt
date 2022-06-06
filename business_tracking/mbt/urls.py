from django.urls import path

from . import views 

app_name = "mbt"

urlpatterns = [
    path('',views.inbound, name="inbound"),
    path('<int:inbound_id>/', views.inbound_detail, name='inbound_detail'),
    path('inbound/transfer/<int:inbound_id>', views.inbound_to_contract, name="inbound_to_contract"),
    path('inbound/addact/<int:inbound_id>', views.add_inbound_history, name="add_inbound_action"),
    path('inbound/create/', views.create_inbound, name='create_inbound'),
]