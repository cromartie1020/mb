
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls') ),
    path('accounts/', include('accounts.urls')),
    path('',include('post.urls')),
    path('admin/', admin.site.urls),
    
]
