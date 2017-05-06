from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice

# Create your views here.
def index(request):
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html')


def marble(request):
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/marbles.html')

def wishlist(request):
    return render(request,'polls/wishlist.html')