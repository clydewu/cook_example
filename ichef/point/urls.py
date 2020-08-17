# -*- coding:utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('import', views.import_point, name='import_point'),
    path('old_import', views.old_import_point, name='import_point'),
]
