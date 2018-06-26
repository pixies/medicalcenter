from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from blog.models import Noticia

def index(request):
    noticias = Noticia.objects.all().order_by('-published_date')

    context = {
        'noticias': noticias
    }

    return render(request, 'blog/blog.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    print(post)
    return render(request, 'blog/post_detail.html', {'post': post})