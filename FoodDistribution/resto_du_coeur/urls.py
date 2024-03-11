# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     ]


from django.urls import path
from .views import (
    HomeView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryDetailView,
    DistributionSiteListView,
    detail,
    index,
    checkout,
 
)

urlpatterns = [
    path('', index, name='index'), # Vue d'accueil
    path('detail/<int:myid>/', detail, name='detail'), # Vue de détail
    path('home', checkout, name='checkout'),
    path('checkout', HomeView.as_view(), name='index'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('sites/', DistributionSiteListView.as_view(), name='site-list'),
   
 
]
