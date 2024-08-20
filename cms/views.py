from django.shortcuts import render, get_object_or_404
from .models import Page
from django.shortcuts import redirect

def redirect_to_first_page(request):
    return redirect('page_detail', slug='your-default-page-slug')



def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'cms/page_detail.html', {'page': page})

def home(request):
    return render(request, 'home.html')