from django.shortcuts import render
from reportage.models import Reportage
from django.db.models import Count
from category.models import Category

# Create your views here.


def home_view(request, *args, **kwargs):
    reportages = Reportage.objects.all()
    top_reportages = select_top_reportages()
    top_reportage = top_reportages[0]
    top_reportages = top_reportages[1:4]
    categories = Category.objects.all()
    context = {
        "top_reportage": top_reportage,
        "top_reportages": top_reportages,
        "reportages": reportages,
        "categories": categories,

    }
    return render(request, 'home/index.html', context=context)


def select_top_reportages():
    top_reportage = Reportage.objects.annotate(
        likes_count=Count('likes')).order_by('-likes_count')[:4]

    # top_reportage = Reportage.objects.all().order_by('likes')
    print(top_reportage)
    return top_reportage
