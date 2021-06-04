"""apiproject URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from apiapp.views import CountryViewSet, StateViewSet, AddressViewSet, AddressDetailViewSet
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register("countries", CountryViewSet)
router.register("states", StateViewSet)
router.register("address", AddressViewSet)
router.register("address_detail", AddressDetailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projectapi/", include(router.urls)),
    path('projectapi/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('projectapi/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]