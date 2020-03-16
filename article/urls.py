from django.urls import path
from .views import (
    ArticleView,
    MainSlideView,
    DetailView
)

urlpatterns = [
    path('/<int:article_types_id>', ArticleView.as_view()),
    path('/main-slide', MainSlideView.as_view()),
    path('/detail/<int:id>', DetailView.as_view()),
]
