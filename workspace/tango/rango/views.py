from django.http import request
from django.shortcuts import render
from rango.models import Category, Page
import random
from rango.forms import CategoryForm, PageForm

# Create your views here.


def rango(request):
    categories = Category.objects.order_by('likes')
    context = {'categories': categories}
    return render(request, 'rango/rango.html', context)


def about(request):
    return render(request, 'rango/about.html')


def populate(request):
    # Python
    pythonCategory = popCategory('Python')
    popPage(category=pythonCategory,
            title='Official Python Tutorial',
            url='http://docs.python.org/2/tutorial/')
    popPage(category=pythonCategory,
            title='How to Think like a Computer Scientist',
            url='http://www.greenteapress.com/thinkpython/')
    popPage(category=pythonCategory,
            title='Learn Python in 10 Minutes',
            url='http://www.korokithakis.net/tutorials/python/')
    # Django
    djangoCategory = popCategory('Django')
    popPage(category=djangoCategory,
            title='Official Django Tutorial',
            url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')
    popPage(category=djangoCategory,
            title='Django Rocks',
            url='http://www.djangorocks.com/')
    popPage(category=djangoCategory,
            title='How to Tango with Django',
            url='http://www.tangowithdjango.com/')
    # Other frameword
    frameCategory = popCategory('Other Frameworks')
    popPage(category=frameCategory,
            title='Bottle',
            url='http://bottlepy.org/docs/dev/')
    popPage(category=frameCategory,
            title='Flask',
            url='http://flask.pocoo.org')


def popCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0, 20)
    category.likes = random.randint(0, 20)
    category.save()
    return category


def popPage(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title,
                                      url=url, views=views)[0]
    page.save()


def category(request, categoryNameSlug):
    context = {}
    try:
        category = Category.objects.get(slug=categoryNameSlug)
        context['category'] = category
        pages = Page.objects.filter(category=category)
        context['pages'] = pages
    except Category.DoesNotExist:
        context['categoryName'] = categoryNameSlug.replace('',	' ')
    return render(request, 'rango/category.html', context)


def addCategory(request):
    template = 'rango/addCategory.html'
    if request.method == 'GET':
        return render(request, template, {'form': CategoryForm()})

    # request.method=='POST'
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form': form})

    form.save(commit=True)
    return rango(request)  # Call function rango()


def addPage(request, categoryNameSlug):
    template = 'rango/addPage.html'
    try:
        cat = Category.objects.get(slug=categoryNameSlug)
    except Category.DoesNotExist:
        return category(request, categoryNameSlug)

    context = {'category': cat}
    if request.method == 'GET':
        context['form'] = PageForm()
        return render(request, template, context)

    # request.method=='POST'
    form = PageForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, template, context)
    page = form.save(commit=False)
    page.category = cat
    page.views = 0
    page.save()
    return category(request, categoryNameSlug)
