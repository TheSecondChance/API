from django.contrib import admin
from django.urls import path
from .views import personDetail, personid
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personDetail/', personDetail),
    path('personDetail/<int:id>', personid)
]

urlpatterns = format_suffix_patterns(urlpatterns)