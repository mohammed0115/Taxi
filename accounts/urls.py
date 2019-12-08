from django.urls import include, path
from rest_framework import routers
from accounts import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/login/', views.Login.as_view(), name='login'),
    path('api/Registeration/', views.Register.as_view(), name='Registeration'),
    path('api/Users/', views.UsersViews.as_view(), name='UsersViews'),
    path('api/Users/<int:pk>/', views.UserViews.as_view(), name='UserViews'),



]