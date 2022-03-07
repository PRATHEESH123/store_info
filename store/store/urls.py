"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import ProductViewSet,CategoryViewSet
from django.conf.urls import url, include

# 3rd party
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

admin.site.site_header = 'Beinex Task'
admin.site.site_title = 'Beinex Task'
admin.site.index_title = 'Home'
admin.site.site_url = "https://www.Beinex-Task.in/"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
