from django.urls import path
from .views import (
    QuizView,
    QuizStartView
)

urlpatterns = [
    path('', QuizView.as_view()),
    path('/start', QuizStartView.as_view()),
]
