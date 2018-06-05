from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.AllBlogsView.as_view(), name='allblogs'),
    path('<int:pk>/', views.BlogView.as_view(), name='detail'),

]
