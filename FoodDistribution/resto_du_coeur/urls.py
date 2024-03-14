# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     ]


from django.urls import path
from .views import *


urlpatterns = [

    #Admin 
    path('list', product_seller_list, name='produtListSeller'),
    path('addproduct',  addProduct, name=' addproduct'),
    path('modifier/<int:pk>', EditViewProduct.as_view(), name='produit_detail'),
    path('supprimer/<int:pk>', DeleteViewProduct.as_view(), name='supprimmer_produit'),


    # Client
    path('', index, name='index'), # Vue d'accueil
    path('detail/<int:myid>/', detail, name='detail'), # Vue de détail
    path('home', checkout, name='checkout'),
    path('checkout', HomeView.as_view(), name='index'),


    path('sites/', DistributionSiteListView.as_view(), name='site-list'),
   


]
