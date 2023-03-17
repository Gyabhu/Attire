from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(), name = "home"),
    path('shop',ShopView.as_view(), name = "shop"),
    path('cart',CartView.as_view(), name = "cart"),
    path('contact',ContactView.as_view(), name = "contact"),
    path('about',AboutView.as_view(), name = "about"),
    path('product-detail',ProductDetailView.as_view(), name = "product-detail"),
    path('signup',signup, name = "signup"),
    path('signin',signin, name = "signin"),
]