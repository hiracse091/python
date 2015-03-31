from django.shortcuts import render_to_response
from article.models import Article

# Create your views here.
def articles(request):
    return  render_to_response('article/articles.html',
                                {'articles':Article.objects.all()})
def article(request, article_id=1):
    return render_to_response('article/article.html',
        {'article':Article.objects.get(id=article_id)})
