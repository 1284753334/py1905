

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"
urlpatterns = [

    path("test",views.test ,name = "test"),
    path("test",views.test ,name = "test"),


]