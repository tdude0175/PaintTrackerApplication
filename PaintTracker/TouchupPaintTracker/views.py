from django.shortcuts import render
from django.http import HttpResponse , Http404
from .forms import TouchUpPaint , TouchUpForm

def index(request):
    return render(request, 'TouchupPaintTracker/index.html')


def renderPaintList(request):
    touchUpPaintlist = TouchUpPaint.objects.all()
    context = {
        'Paints':touchUpPaintlist
    }
    return render(request, 'TouchupPaintTracker/paintList.html',context)

def addNewPaint(request):
    return render(request, 'TouchupPaintTracker/addNewPaint.html')
# Create your views here.
