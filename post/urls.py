from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list,name='home'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_form, name='new'),
    path('edit/<int:id>/', views.post_edit, name='edit'),
    path('delete/<int:id>/', views.post_delete, name='delete'),
    

]
