from django.shortcuts import redirect, render
from .models import *

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

    
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Category, DistributionSite, Product, Order, OrderItem
# from .serializers import CategorySerializer, DistributionSiteSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer

# class CategoryListView(ListView):
#     model = Category

# class CategoryCreateView(CreateView):
#     model = Category
#     fields = '__all__'

# class CategoryUpdateView(UpdateView):
#     model = Category
#     fields = '__all__'

# class CategoryDeleteView(DeleteView):
#     model = Category

# class CategoryDetailView(DetailView):
#     model = Category

# class DistributionSiteListView(ListView):
#     model = DistributionSite

# class DistributionSiteCreateView(CreateView):
#     model = DistributionSite
#     fields = '__all__'

# class DistributionSiteUpdateView(UpdateView):
#     model = DistributionSite
#     fields = '__all__'

# class DistributionSiteDeleteView(DeleteView):
#     model = DistributionSite

# class DistributionSiteDetailView(DetailView):
#     model = DistributionSite











from django.shortcuts import render
from django.views import View

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