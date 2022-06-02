from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('product/', views.productt, name='product'),
    path('search/', views.search, name='search'),
    path('productDetails/<int:id>/', views.productDetails, name='productDetails'),
    path('^comments/', views.comments, name='comments'),
    path('payment/', views.payment, name='payment'),
]