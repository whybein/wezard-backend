from django.urls import path
from .views import (
    NewsView, 
    FeatureView, 
    LatestNewsView, 
    MagicalFeatureView, 
    MainSlideView
)

urlpatterns = [
    path('/news', NewsView.as_view()),
    path('/feature', FeatureView.as_view()),
    path('/latest-news', LatestNewsView.as_view()),
    path('/magical-features', MagicalFeatureView.as_view()),
    path('/main-slide', MainSlideView.as_view()),
]
