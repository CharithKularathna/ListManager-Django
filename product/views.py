from django.shortcuts import render
from product.functions import *

# Create your views here.

def index(request):
    pList = getLists('product_list.txt')
    context = {'pList':pList}
    return render(request,"product/index.html",context)

def search(request):
    search_str = request.POST['search']
    context = {'search_str':search_str}
    return render(request,"product/search.html",context)

