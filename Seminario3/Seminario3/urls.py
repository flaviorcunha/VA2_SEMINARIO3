from django.contrib import admin
from django.urls import path, include
from VA2.views import ClienteViewSet
from OAT.views import ProfessorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'cliente', ClienteViewSet) 
router.register (r'professor', ProfessorViewSet) 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))

]
