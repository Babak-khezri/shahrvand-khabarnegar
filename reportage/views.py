from django.shortcuts import render
from .models import Reportage
# Create your views here.


def reportage_detail(request, pk):
    reportage = Reportage.objects.get(pk=pk)
    context = {
        'reportage': reportage,
    }
    return render(request, 'reportage/reportage_detail.html', context=context)
