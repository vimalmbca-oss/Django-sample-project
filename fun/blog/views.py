from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
import logging

# posts = [
#           {'id':1,'title':'post 1','content':"hello python",'word':'python'},
#           {'id':2,'title':'post 2','content':"hello java",'word':'java'},
#           {'id':3,'title':'post 3','content':"hello html",'word':'html'},
#           {'id':4,'title':'post 4','content':"hello css",'word':'css'},
#           {'id':5,'title':'post 5','content':"hello javascript",'word':'javascript'},
#           {'id':6,'title':'post 6','content':"hello mysql",'word':'mysql'}
#      ]

def main(request):
     blog_title = 'NEW POST'
     posts = Post.objects.all() 
     paginator = Paginator(posts,5)
     page_number = request.GET.get('page')
     page_abj = paginator.get_page(page_number)    
     return render(request, 'index.html',{'blog_title':blog_title,'page_abj':page_abj})

def detail(request,slug):

     # post = next((item for item in posts if item['id'] == id),None)
     post = Post.objects.get(slug=slug)
     related_posts = Post.objects.filter(category = post.category).exclude(pk = post.id)
     return render(request, 'detail.html',{'post':post,'related_posts':related_posts})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        logger = logging.getLogger("TESTING") # type: ignore
        if form.is_valid():
            logger.debug(f"POST DATA is : {form.cleaned_data['name']}{form.cleaned_data['email']}{form.cleaned_data['message']}")
            success_message = "Your message has been sent successfully!"
            return render(request, "contact.html", {"form": form, "success_message": success_message})
        else:
            logger.debug("Form is not valid")
        return render(request, "contact.html", {"form": form, "name": name, "email": email, "message": message})
    return render(request, "contact.html")
   

