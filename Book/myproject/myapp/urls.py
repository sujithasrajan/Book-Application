from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
path('',views.book_list),
]
