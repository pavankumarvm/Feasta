"""feasta URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

# remove in production
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def api(prefix=None):
    """
    :param prefix:
    :return: Base url for API
    """
    if prefix is None:
        return "api/v1/"
    else:
        return "api/v1/{}".format(prefix)

from accounts.views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path(api(), include('mess.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/v1/allauth/', include('allauth.urls')),
]

