from django.contrib import admin
from django.urls import include, path
from register import views as registerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerViews.register, name='register'),
    path('', include("main.urls"))
]
