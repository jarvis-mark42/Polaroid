from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, RequestContext
from BlackHeart.settings import TEMPLATE_DIR
from django import forms
from BeautifulSoup import BeautifulSoup

class signinForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

# Create your views here.
def home(request):
    t = Template(open(TEMPLATE_DIR+"homepage.html").read())
    return HttpResponse(t.render(Context({})))

def signin(request):
    form = signinForm()
    if request.method == 'POST':
        form = signinForm(request.POST)
        print (request.POST[u'username'])
        print (request.POST[u'password'])
        if form.is_valid():
            return HttpResponseRedirect('/thanks/');
        else:
            form = signinForm()
    #return render(request,"/home/jarvis/BlackHeart/templates/signin.html",{'form':form})
    t = Template(open(TEMPLATE_DIR+"signin.html").read())
    return HttpResponse(t.render(RequestContext(request,{'form':form})))

def thank(request):
    return HttpResponse('Thanks')