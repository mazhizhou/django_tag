from django.shortcuts import render, render_to_response
from blog.models import BlogsPost

# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})
	
def blog_bs_test(request):
	return render_to_response('bootstrap_test.html')
	
def blog_head_test(request):
	return render_to_response('head_test.html')
	
