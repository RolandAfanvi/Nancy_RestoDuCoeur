import json
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Category, DistributionSite, Product, Order, OrderItem

def serialize_model(model_instance):
    serialized_data = serialize('json', [model_instance])
    deserialized_data = json.loads(serialized_data)
    return deserialized_data[0]['fields']

def category_list(request):
    categories = Category.objects.all()
    serialized_categories = [serialize_model(category) for category in categories]
    return JsonResponse(serialized_categories, safe=False)

def distribution_site_list(request):
    sites = DistributionSite.objects.all()
    serialized_sites = [serialize_model(site) for site in sites]
    return JsonResponse(serialized_sites, safe=False)
