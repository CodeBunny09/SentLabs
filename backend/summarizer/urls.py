from django.urls import path
from .views import TextDataListCreateView

urlpatterns = [
    path('summarize/', TextDataListCreateView.as_view(), name='summarize')
]
