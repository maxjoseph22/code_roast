from django.urls import path
from . import views
from submissions.views import submission_detail, new

urlpatterns = [
    path('<int:id>', submission_detail, name='submission_detail'),
    path('new', new, name='new'),
]