from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

from django.views import View

#home
def index(request):
    product_object = Product.objects.all()
    categories = Category.objects.all()
    item_name = request.GET.get('item')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(name__icontains=item_name)
    paginator = Paginator(product_object, 8)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'index.html', {'produits': product_object, 'categories':categories})

#detail
def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'detail.html', {'product': product_object})    


def checkout(request):
    return render(request, 'checkout.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})

class CategoryCreateView(View):
    def get(self, request):
        # Logique pour afficher le formulaire de création de catégorie
        return render(request, 'category_form.html')

    def post(self, request):
        # Logique pour traiter les données du formulaire de création de catégorie
        return redirect('category_list')

class CategoryDetailView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        return render(request, 'category_detail.html', {'category': category})

class CategoryUpdateView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        return render(request, 'category_update.html', {'category': category})

    def post(self, request, category_id):
        category = Category.objects.get(id=category_id)
        # Logique pour mettre à jour la catégorie
        return redirect('category_list')

class CategoryDeleteView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        return render(request, 'category_confirm_delete.html', {'category': category})

    def post(self, request, category_id):
        category = Category.objects.get(id=category_id)
        # Logique pour supprimer la catégorie
        return redirect('category_list')

class DistributionSiteListView(View):
    def get(self, request):
        distribution_sites = DistributionSite.objects.all()
        return render(request, 'distribution_site_list.html', {'distribution_sites': distribution_sites})