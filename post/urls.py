from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list,name='home'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    
]
