# pages/urls.py
from django.urls import path

from .views import homePageView, CoordinatorView, CatView, IntakeSourceView, FosterHomeView

urlpatterns = [
    path('', homePageView, name='home'),
    path('coordinator', CoordinatorView.as_view(), name='Coordinator'),
    path('cat', CatView.as_view(), name='Cat'),
    path('intake', IntakeSourceView.as_view(), name='IntakeSource'),
    path('fosterhome', FosterHomeView.as_view(), name='FosterHome')
]
