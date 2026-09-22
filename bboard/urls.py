from django.urls import path
from django.views.generic import CreateView
from .models import Bb

from .views import index, by_rubric, add_and_save
app_name = 'bboard'


urlpatterns = [
    path('add/', add_and_save, name='add'),
    #path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]