"""Back_End_Taxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from Categories.views import CategoriesViewSet
from Journey.views import JourneyViewSet
from License.views import LicenseViewSet
from Vehicle.views import VehicleViewSet
from rest_framework import routers
from accounts.views import driverViewSet,ClientViewSet

router = routers.DefaultRouter()
router.register('Categories', CategoriesViewSet)
router.register('Journey', JourneyViewSet)
router.register('License', LicenseViewSet)
router.register('Vehicle', VehicleViewSet)
router.register('driver', driverViewSet)
router.register('client', ClientViewSet)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('API/',include(router.urls)),

]
