from django.urls import path

# from .views import MessOwnerSignUpView,ConsumerSignUpView
from .views import FeastaUserViewSet, MessOwnerViewSet, ConsumerViewSet
from .views import HomePageView

urlpatterns = [
    path('get-user/', FeastaUserViewSet.as_view({
        'get': 'get',
        'post': 'post',
    })),
    path('get-user/<str:username>/', FeastaUserViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),
    path('get-messowner/', MessOwnerViewSet.as_view({
        'get': 'get',
        'post': 'post',
    })),
    path('get-messowner/<str:user>/', MessOwnerViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),
    path('get-consumer/', ConsumerViewSet.as_view({
        'get': 'get',
        'post': 'post',
    })),
    path('get-consumer/<str:user>/', ConsumerViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),
]
