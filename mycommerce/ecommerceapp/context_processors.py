from . models import Category

def cat_link(request):
    links=Category.objects.all()
    return dict(links=links)