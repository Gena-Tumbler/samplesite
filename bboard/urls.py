from django.urls import path
from django.views.generic import CreateView
from .models import Bb

from .views import index, BbAddView, BbEditView, BbByRubricView, BbDeleteView #by_rubric, add_and_save,
app_name = 'bboard'


urlpatterns = [
    path('add/', BbAddView.as_view(), name='add'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    #path('add/', add_and_save, name='add'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    #path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    #path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]