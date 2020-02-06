
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('',views.main,name='main')
]
