from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search, name='search'),
    path('add/',views.add,name='add'),
    path('addResult/',views.addResult,name='addResult')
]
