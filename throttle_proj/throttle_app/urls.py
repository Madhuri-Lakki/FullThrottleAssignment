from django.contrib import admin
from django.urls import path
from throttle_app import views

urlpatterns = [
    ##path('admin/', admin.site.urls),
    path('posts',views.Throttledataposts),
    path('gets',views.ThrottledataGets)
]