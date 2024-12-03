from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')


def username(request):
    users = User.objects.all()
    for user in users:
        return HttpResponse(f"{user.username} {user.email}")

    return ""


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html', {'tweets': tweets})


def tweet_create(request):

    if request.method =="POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=false)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

        
    else :
        form = TweetForm()

    return render(request,Tweet_form.html,{'form':form})


def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user= request.user)
    if request.method =="POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

        
    else:
        form = TweetForm(instance=tweet)
    
    return render(request,Tweet_form.html,{'form':form})

def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request,Tweet_confirm_delete.html,{'tweet':tweet}) 