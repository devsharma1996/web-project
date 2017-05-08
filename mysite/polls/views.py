from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.

html_content=''

def index(request):
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html')


def marble(request):
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/marbles.html')

def wishlist(request):
    for name,value in request.COOKIES.items():
        print ("key:"+name)
        print ("value:"+value)
    html_content=render_to_string('polls/wishlist.html',{'cookies':request.COOKIES})
    html_content=render(request,'polls/wishlist.html',{'cookies':request.COOKIES})
    return html_content

def vote(request):
    to=request.POST['choice']
    print(to)
    #send_mail(
    #'Subject here',
    #'Here is the message.',
    #'devsharmarouth132@gmail.com',
    #[to],
    #fail_silently=False,
    #)
    #rendered = render_to_string('polls/wishlist.html')
    #html_content=rendered
    html_content=render_to_string('polls/wishlist.html',{'cookies':request.COOKIES})   
    
    
    msg = EmailMessage('email fro arm', html_content,'devsharmarouth132@gmail.com', [to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return HttpResponseRedirect(reverse('polls:wishlist'))
    
    