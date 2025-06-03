from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('merch/', views.merch_index, name='merch-index'),

]
