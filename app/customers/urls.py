from django.urls import path, re_path
from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    re_path('^customers/(?P<registration>.+)/$', views.CustomertDetail.as_view()),
]