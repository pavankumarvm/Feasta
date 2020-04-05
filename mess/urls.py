from django.urls import path
from mess.views import MessApiView, MenuApiView
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('get-mess/', MessApiView.as_view({'get': 'get', 'post': 'post'}), name="mess-api-view"),
    path('get-mess/<str:id>/', MessApiView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })),
    path('get-menu/', MenuApiView.as_view({'get': 'get', 'post': 'post'}), name ="menu-api-view"),
    path('get-menu/<str:menu_id>/', MenuApiView.as_view({
        'get': 'get_data',
        'delete': 'destroy',
        'put': 'update'
    }))
]
