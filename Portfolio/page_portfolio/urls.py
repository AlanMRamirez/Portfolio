from django.urls import path
from .views import ProjectsListView

app_name = 'page_portfolio'

urlpatterns = [
    path('', ProjectsListView.as_view(), name='portfolio'),
]
