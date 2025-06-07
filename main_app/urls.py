from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('merch/', views.merch_index, name='merch-index'), 
    path('merch/user/', views.user_merch_index, name='user-merch-index'), 
    path('merch/<int:item_id>/', views.merch_detail, name='merch-detail'),
    path('merch/create/', views.ItemCreate.as_view(), name='merch-create'),
    path('merch/<int:pk>/update/', views.ItemUpdate.as_view(), name='merch-update'),
    path('merch/<int:pk>/delete/', views.ItemDelete.as_view(), name='merch-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('merch/<int:item_id>/comment/', views.add_comment, name='add_comment')
]
