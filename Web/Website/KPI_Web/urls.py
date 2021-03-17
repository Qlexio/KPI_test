from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('investments/', views.investments, name="investments"),
    path("city/", views.investments_by_city, name="investmentsbycity"),
    path("progress/", views.investments_by_progress, name="investmentsbyprogress"),
    path("code/", views.investments_by_code, name="investmentsbycode"),
    path("city_progress/", views.investments_by_city_progress, name="investmentsbycityprogress"),
    path("new/", views.new_investment, name="newinvestments"),
    path("map/", views.investments_map, name="investmentsmap"),
]
