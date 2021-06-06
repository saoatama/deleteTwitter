from django.http import HttpResponse
from django.template import loader
import tweepy
from django.conf import settings
from django.shortcuts import redirect

def index(request):
    context = {
    }
    template = loader.get_template('mainFunction/index.html')
    return HttpResponse(template.render(context, request))

def post(request):
    consumer_token = settings.CONSUMER_TOKEN
    consumer_secret = settings.CONSUMER_SECRET
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    redirect_url = auth.get_authorization_url()

    return redirect(redirect_url)

def continue_delete(request):
    context = {
    'consumer_token': settings.CONSUMER_TOKEN,
    'consumer_secret': settings.CONSUMER_SECRET,
    }
    template = loader.get_template('mainFunction/continue_delete.html')
    return HttpResponse(template.render(context, request))
