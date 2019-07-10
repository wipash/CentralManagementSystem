# pages/urls.py
from django.urls import path

from .views import homePageView, CoordinatorView

urlpatterns = [
    path('', homePageView, name='home'),
    path('coordinator', CoordinatorView, name='cats')
]
