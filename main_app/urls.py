from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('merch/', views.merch_index, name='merch-index'), 
    path('merch/<int:item_id>/', views.merch_detail, name='merch-detail'),
    path('merch/create/', views.ItemCreate.as_view(), name='merch-create'),
]
