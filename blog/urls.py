from django.urls import path

from . import views
app_name="blog"

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name='home'),
]