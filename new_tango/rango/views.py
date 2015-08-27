from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rango.models import *
from rango.form import *

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


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print form.errors

    else:
        form = PageForm()
    return render(request,'rango/add_page.html',{'form': form})