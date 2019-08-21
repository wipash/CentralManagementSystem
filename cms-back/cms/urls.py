# pages/urls.py
from django.urls import path

from .views import homePageView, CoordinatorView, CoordinatorDetailView, CatView, CatDetailView, IntakeSourceDetailView, IntakeSourceView, FosterHomeView, FosterHomeDetailView

urlpatterns = [
    path('', homePageView, name='home'),
    path('coordinator', CoordinatorView.as_view(), name='Coordinator'),
    path('coordinatorID/<int:pk>/', CoordinatorDetailView.as_view(), name='CoordinatorID'),
    path('cat', CatView.as_view(), name='Cat'),
    path('catID/<int:catID>/', CatDetailView.as_view(), name='CatID'),
    path('intake', IntakeSourceView.as_view(), name='IntakeSource'),
    path('intakeID/<int:pk>/', IntakeSourceDetailView.as_view(), name='IntakeID'),
    path('fosterhome', FosterHomeView.as_view(), name='FosterHome'),
    path('fosterhomeID/<int:pk>/', FosterHomeDetailView.as_view(), name='FosterHomeID'),
]
