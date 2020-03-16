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
    path('/latestnews', LatestNewsView.as_view()),
    path('/magicalfeatures', MagicalFeatureView.as_view()),
    path('/mainslide', MainSlideView.as_view()),
]
