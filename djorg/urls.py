"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework import routers 
from notes.api import PersonalNoteViewSet


from rest_framework.authtoken import views
#The ^ is means "match the beginning of the string" in a regular expression. 
# The re_path function is just like path, 
# except it interprets the endpoint as a regex instead of a fixed string.

router = routers.DefaultRouter()
router.register('notes', PersonalNoteViewSet)
#router.register('goats', PersonalGoatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), #takes all endpoints in router
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]

#This will set the path to /api/notes. We can use router.register to add as many paths 
# as we want this way, without needing to add them to urlpatterns