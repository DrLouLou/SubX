from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from subscriptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('subscriptions/<int:subscription_id>/', views.subscription_detail, name='subscription_detail'),
]


