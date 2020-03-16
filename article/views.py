import random

from .models import Article

from django.views import View
from django.http import JsonResponse

class NewsView(View):
    def get(self, request):
        news_list = [
            {
                'title' : news.title,
                'author' : news.author,
                'thumbnail' : news.thumbnail,
            }for news in Article.objects.filter(article_types__id=1)
        ]
        return JsonResponse({'data': news_list}, status = 200)

class FeatureView(View):
    def get(self, request):
        feature_list = [
            {
                'title' : feature.title,
                'author' : feature.author,
                'thumbnail' : feature.thumbnail,
            }for feature in Article.objects.filter(article_types__id=2)
        ]        
        return JsonResponse({'data': feature_list}, status = 200)

class LatestNewsView(View):
    def get(self, request):
        items = 3
        news_list = [
            {
                'title' : news.title,
                'thumbnail' : news.thumbnail,
            }for news in Article.objects.filter(article_types__id=1).order_by('-created_at')
        ][:items]

        return JsonResponse({'data':news_list}, status = 200)

class MagicalFeatureView(View):
    def get(self, request):
        item = 4
        feature_list = [
            {
                'title' : features.title,
                'thumbnail' : features.thumbnail
            }for features in Article.objects.filter(article_types__id=2)
        ]
        just_3_feature_list = random.sample(feature_list, item)

        return JsonResponse({'data':just_3_feature_list}, status = 200)

class MainSlideView(View):
    def get(self, request):
        items =3
        item = 4
        
        mainslide_feature_list = [
            {
                'title' : features.title,
                'thumbnail' : features.thumbnail,
            }for features in Article.objects.filter(article_types__id=2)
        ]
        just_3_feature_list = random.sample(mainslide_feature_list, item)

        mainslide_7list = just_3_feature_list + [
            {
                'title' : news.title,
                'thumbnail' : news.thumbnail,
            }for news in Article.objects.filter(article_types__id=1).order_by('?')
        ][:items]

        return JsonResponse({'data':mainslide_7list}, status = 200)
