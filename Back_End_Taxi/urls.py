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
# class SearchForTrip(APIView):
from Journey.views import JourneyViewSet,SearchForTrip
from License.views import LicenseViewSet
from Vehicle.views import VehicleViewSet
from rest_framework import routers
from accounts.views import driverViewSet,ClientViewSet

router = routers.DefaultRouter()
# router.register('Categories', CategoriesViewSet)
# router.register('License', LicenseViewSet)
# router.register('Vehicle', VehicleViewSet)
# router.register('driver', driverViewSet)
# router.register('client', ClientViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # path('API/',include(router.urls)),
    path('API/Journey/', JourneyViewSet.as_view({'post': 'create'})),
    path('API/Journey/<int:pk>/', JourneyViewSet.as_view({'put': 'update','put':'partial_update'})),
    path('API/Journey/search/', SearchForTrip.as_view()),
    path('API/Journey/all/', JourneyViewSet.as_view({'post': 'list'})),



    # Categories
    path('API/Categories/all/', CategoriesViewSet.as_view({'post': 'list'})),
    path('API/Categories/create/', CategoriesViewSet.as_view({'post':'create'})),
    path('API/Categories/retrieve/<int:pk>/', CategoriesViewSet.as_view({'post':'retrieve'})),
    path('API/Categories/update/<int:pk>/', CategoriesViewSet.as_view({'put':'update'})),
    path('API/Categories/partial_update/<int:pk>/', CategoriesViewSet.as_view({'put':'partial_update'})),

    # License
    path('API/License/all/', LicenseViewSet.as_view({'post': 'list'})),
    path('API/License/create/', LicenseViewSet.as_view({'post':'create'})),
    path('API/License/retrieve/<int:pk>/', LicenseViewSet.as_view({'post':'retrieve'})),
    path('API/License/update/<int:pk>/', LicenseViewSet.as_view({'put':'update'})),
    path('API/License/partial_update/<int:pk>/', LicenseViewSet.as_view({'put':'partial_update'})),

    # Vehicle
    path('API/Vehicle/all/', VehicleViewSet.as_view({'post': 'list'})),
    path('API/Vehicle/create/', VehicleViewSet.as_view({'post':'create'})),
    path('API/Vehicle/retrieve/<int:pk>/', VehicleViewSet.as_view({'post':'retrieve'})),
    path('API/Vehicle/update/<int:pk>/', VehicleViewSet.as_view({'put':'update'})),
    path('API/Vehicle/partial_update/<int:pk>/', VehicleViewSet.as_view({'put':'partial_update'})),


    # driver
    path('API/driver/all/', driverViewSet.as_view({'post': 'list'})),
    path('API/driver/create/', driverViewSet.as_view({'post':'create'})),
    path('API/driver/retrieve/<int:pk>/', driverViewSet.as_view({'post':'retrieve'})),
    path('API/driver/update/<int:pk>/', driverViewSet.as_view({'put':'update'})),
    path('API/driver/partial_update/<int:pk>/', driverViewSet.as_view({'put':'partial_update'})),

   
     # client
    path('API/client/all/', ClientViewSet.as_view({'post': 'list'})),
    path('API/client/create/', ClientViewSet.as_view({'post':'create'})),
    path('API/client/retrieve/<int:pk>/', ClientViewSet.as_view({'post':'retrieve'})),
    path('API/client/update/<int:pk>/', ClientViewSet.as_view({'put':'update'})),
    path('API/client/partial_update/<int:pk>/', ClientViewSet.as_view({'put':'partial_update'})),




]
