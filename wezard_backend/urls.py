from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('sorting', include('sorting.urls')),
    path('article', include('article.urls')),
    path('quiz', include('quiz.urls'))
]
