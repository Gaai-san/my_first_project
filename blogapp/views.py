from django.shortcuts import render, get_object_or_404
from .models import BlogModel

# Create your views here.
def all_blogs(request):
    blogs = BlogModel.objects.order_by('-date')
    return render(request, 'blogapp/all_blogs.html', {'blogs':blogs})

def detail(request, blogapp_id):
    blog = get_object_or_404(BlogModel, pk=blogapp_id)
    return render(request, 'blogapp/detail.html', {'blog':blog})

    