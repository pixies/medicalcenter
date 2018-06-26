from django.shortcuts import render

from website.models import Website

from blog.models import Noticia

def index(request):
    website = Website.objects.get(usuario_id=1)
#    noticias = Noticia.objects.all()
    noticias = Noticia.objects.all().order_by('-published_date')[:3]
    print(noticias)

    head = {
        'title': website.title,
        'scripts': website.list_scripts.all(),
    }

    context = {
        'head': head,
        'noticias': noticias
    }

    return render(request, 'index.html', context=context)

