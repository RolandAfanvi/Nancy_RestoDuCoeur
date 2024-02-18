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
    # DistributionSiteCreateView,
    # DistributionSiteUpdateView,
    # DistributionSiteDeleteView,
    # DistributionSiteDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('sites/', DistributionSiteListView.as_view(), name='site-list'),
    # path('sites/create/', DistributionSiteCreateView.as_view(), name='site-create'),
    # path('sites/update/<int:pk>/', DistributionSiteUpdateView.as_view(), name='site-update'),
    # path('sites/delete/<int:pk>/', DistributionSiteDeleteView.as_view(), name='site-delete'),
    # path('sites/<int:pk>/', DistributionSiteDetailView.as_view(), name='site-detail'),
]