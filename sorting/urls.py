from django.urls import path

from .views import(
    HouseView,
)

urlpatterns = [
    path('/house/<int:question_id>', HouseView.as_view()),
]
