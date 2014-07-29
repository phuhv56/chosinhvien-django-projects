from django.core.context_processors import csrf
from django.core.files.uploadhandler import FileUploadHandler
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from mysite.models import Product, Category, Area
from django.template.loader import get_template
from forms import ProductForm, AnonymousForm
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()

def show_all(request):
    user = ''
    if 'user' in request.COOKIES:
        user = request.COOKIES['user']
    products = Product.objects.all().order_by('-time_post')
    category = Category.objects.all()
    provice = Area.objects.all()

    paginator = Paginator(products, 5)  # show 5 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'products': products, 'user': user, 'categories': category, 'provices': provice}
    return render_to_response('show_all.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    user = product.user
    context = {'product': product, 'user': user}
    return render_to_response('product_detail.html', context)


def create(request):
    if ( request.user.username=='' ):
        Uform = AnonymousForm(prefix='ano')
        Pform = ProductForm(prefix='prd')
        if request.method == 'POST':
            Pform = ProductForm(request.POST, request.FILES, prefix='prd')
            Uform = AnonymousForm(request.POST, prefix='ano')
            if Uform.is_valid() and Pform.is_valid():
                FileUploadHandler(request.FILES['image'])

                u = Uform.save()
                p = Pform.save()

                u.product_id = p.id

                u.save()

                return HttpResponseRedirect('/show/all/')
        else:
            Pform = ProductForm()
            Uform = AnonymousForm()
        args = {}
        args.update(csrf(request))
        args['Pform'] = Pform
        args['Uform'] = Uform
        return render_to_response('create_product_ano.html', args)

    else:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                FileUploadHandler(request.FILES['image'])

                # u=User.objects.get(username=request.user.username)

                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponseRedirect('/show/all/')
        else:
            form = ProductForm()

        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('create_product.html', args)

def search_product(request):
    search_text = request.POST.get('search_text', '')
    category = request.POST.get('category', '')
    category = request.POST.get('provice', '')

    p = Product.objects.get(id=23)
    context = {'product': p}

    return render_to_response('show_all.html', context)