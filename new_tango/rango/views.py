from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rango.models import *
# Create your views here.

def index(request):
    category_list = Category.objects.order_by("-likes")[:5]
    #Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'categories': category_list}
    page_list = Page.objects.order_by('-views')[:5]
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context_dict)
	
def about(request):
    return render(request, 'rango/about.html', {})

def cat(request, category):

    context_dict = {}
    cates = get_object_or_404(Category, name = category)
    context_dict['names'] = cates
    pages_list = Page.objects.filter(category = cates)
    context_dict['pages'] = pages_list

    return render(request,'rango/page.html', context_dict)
