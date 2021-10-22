from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse
# Create your views here.
def index(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html', {'myposts': myposts})
def bloggpost(request ,id ):
    t = True
    post = Blogpost.objects.filter(post_id = id)[0]
    l = Blogpost.objects.filter(post_id = id+1)
    n=1
    p=0
    if not l:
        t = False
    else:
        n = l[0].post_id
    if post:
        p = post.post_id-1
    #print(l.post_id+1)
    return render(request,'blog/bloggpost.html',{'post':post,'t':t,'n': n,'p':p})