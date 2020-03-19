from django.urls import path

from .views import(
    HouseView,
    HouseResultView,
)

urlpatterns = [
    path('/house/<int:question_id>', HouseView.as_view()),
    path('/house/result', HouseResultView.as_view()),
]
