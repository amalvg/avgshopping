from django.urls import path

from cartapp import views

app_name='cartapp'
urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>',views.add_cart,name='add_cart'),
    path('delete/<int:product_id>',views.cart_delete,name='cart_delete'),
    path('remove/<int:product_id>',views.cart_remove,name='cart_remove'),
]