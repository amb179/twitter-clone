

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks      
# # from .models import Photo
# from .forms import PhotoForm


def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the form is valid
        if form.is_valid():
            #yes, save
            form.save()

            #redirect to home
            return HttpResponseRedirect('/')

        else:
            #no, show error
            return HttpResponseRedirect(form.error.as_json())

    #get all posts, limit =20
    posts = Post.objects.all()[:20]

    #show
    return render(request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    #find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    #find post
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")
    return render(request,'edit.html', 
                    {'post': post})


def likes(request, post_id):

    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect('/')    

#def index(request):
    #post = Post.objects.all()
    #ctx = {'posts' : posts}
    #return render(request, 'posts/posts.html', ctx)



def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'post.html', context)



