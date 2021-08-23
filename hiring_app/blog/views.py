from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def job_requirement_survey(request):
    #context = {
        #'posts': Post.objects.all()
    #}
    #return render(request, 'blog/home.html',{'title': 'Survey'}) #context)

    context = {

                 "age": 67

              }
    return render(request, 'blog/home.html', context)#{'title': 'Survey'}, context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})