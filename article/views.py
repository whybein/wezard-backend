from .models import (
    Article, 
    ArticleType
)

from django.views import View
from django.http import JsonResponse
from django.db.models import Q

class ArticleView(View):
    def get(self, request, article_types_id):
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 20))
        latest = bool(request.GET.get('latest', False))
        magical = bool(request.GET.get('magical', False))

        if latest:
            articles = Article.objects.filter(article_types_id=article_types_id).order_by('-created_at')[offset:limit+offset]
            if magical:
                articles = Article.objects.filter(article_types_id=article_types_id).order_by('?')[offset:limit+offset]
        else:
            articles = Article.objects.filter(article_types_id=article_types_id)[offset:limit+offset]
        
        news_list = [
            {
                'title' : article.__dict__['title'],
                'thumbnail' : article.thumbnail,
            }for article in articles
        ]
        
        if not latest:
            for i in range(len(news_list)):
                news_list[i]['author'] = Article.objects.get(title=news_list[i]['title']).author

        return JsonResponse({'data': news_list}, status = 200)

class MainSlideView(View):
    def get(self, request):
        end = int(request.GET.get('end',175))
        step = int(request.GET.get('step',10))        
        slides = Article.objects.select_related('article_types').filter(Q(article_types=1)|Q(article_types=2)).order_by('article_types_id')[:end:step]
        append_list=[]
        for slide in slides:
            mainslide = {
                'name':slide.article_types.name,
                'id':slide.id,
                'title':slide.title,
                'thumbnail':slide.thumbnail
            }
            append_list.append(mainslide)
        
        return JsonResponse({'data':append_list}, status = 200)

class DetailView(View):
    def get(self, request, id):
        detailview = [{
            'id': article.id,
            'title': article.title,
            'author': article.author,
            'thumbnail': article.thumbnail,
            'content': article.content,
            'created_at': article.created_at,          
        }for article in Article.objects.filter(id=id)]
        return JsonResponse({'data':list(detailview)}, status = 200)