# from django.contrib import admin
# from .models import *
from .views import *
from django.urls import path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('create_data',create_data.as_view(),name='create_data'),
    path('read_data',read_data.as_view(),name='read_data'),
    path('update_data/<str:pk>/',update_data.as_view(), name='update_data'),
    path('delete_data/<str:pk>/',delete_data.as_view(), name='delete_data'),
]