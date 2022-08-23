from django.shortcuts import render
from ecapp.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    query=None
    products=None
    if 'q' in request.GET:
        query= request.GET.get('q')
        products= Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})