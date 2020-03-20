from django.urls import path

from .views import(
    HouseView,
    HouseResultView,
    PassportView,
)

urlpatterns = [
    path('/house/<int:question_id>', HouseView.as_view()),
    path('/house/result', HouseResultView.as_view()),
    path('/passport', PassportView.as_view()),
]
