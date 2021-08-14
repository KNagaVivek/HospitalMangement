from django import urls
from django.conf.urls import url
from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("pharmacy", views.pharmacy,name="pharmacy"),
    path("about", views.about,name="about"),
    path("shop", views.shop,name="shop"),
    path("shop-single1", views.shop_single1,name="shop-single1"),
    path("shop-single2", views.shop_single2,name="shop-single2"),
    path("shop-single3", views.shop_single3,name="shop-single3"),
    path("shop-single4", views.shop_single4,name="shop-single4"),
    path("shop-single5", views.shop_single5,name="shop-single5"),
    path("shop-single6", views.shop_single6,name="shop-single6"),
    path("cart", views.cart,name="cart"),
    url(r'^delete_person/(?P<pk>\d+)/$', views.delete, name='delete_person'),
    path("checkout", views.checkout,name="checkout"),
    path("thankyou", views.thankyou,name="thankyou")
]