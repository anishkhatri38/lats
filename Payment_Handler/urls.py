from django.contrib import admin
from django.urls import path, include
from . import views 



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('plans/<int:pk>', views.plan, name='plan'),
#     path('auth/', include('django.contrib.auth.urls')),
#     path('auth/signup', views.SignUp.as_view(), name='signup'),
#     path('join', views.join, name='join'),
#     path('checkout', views.checkout, name='checkout'),
#     path('auth/settings', views.settings, name='settings'),
#     path('updateaccounts', views.updateaccounts, name='updateaccounts'),
# ]
urlpatterns = [
    path('',views.payment, name = "payment"),
    path('', views.home, name='home'),
    path('join', views.join, name='join'),
    path('auth/settings', views.settings, name='settings'),
     path('checkout', views.checkout, name='checkout'),
    # path('product_checkout/',views.product_checkout, name = "product_checkout"),
    # path('product_cart/',views.product_cart, name = "product_cart"),

    #  path('update_item/',views.updateItem, name = "update_item"),
]