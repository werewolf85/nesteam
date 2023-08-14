"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from games.views import games_list
# from games.views import studios_list
from django.urls import path, include, re_path
from rest_framework import permissions
from games.views import *
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="ixbox85@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)
router.register(r'apistudio', StudioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('games/', games_list, name='games'),
    # path('studios/', studios_list, name='studios'),
    # path('create-game/', CreateGameAPIView.as_view(), name='create-game'),
    path('games/', GamesView.as_view(), name='games'),
    path('game-create/', GameCreateAPIView.as_view(), name='games'),
    path('studios/', StudiosListAPIView.as_view(), name='games'),
    path('users/', include('usersapp.urls')),
    path('collections/', include('collection.urls')),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]
