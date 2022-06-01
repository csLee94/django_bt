from django.urls import path

from . import views 

app_name = "mbt"

urlpatterns = [
    path('',views.inbound, name="inbound"),
    path('<int:inbound_id>/', views.inbound_detail, name='inbound_detail'),
    path('create_inbound/', views.create_inbound, name='create_inbound'),
]