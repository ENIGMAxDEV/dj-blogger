from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('/about', about, name="about"),
    path('/post/<int:post_id>', post_details, name='post_details')
]
