from django.shortcuts import render
from product.functions import *

# Create your views here.

def index(request):
    pList = getLists('product_list.txt')
    context = {'pList':pList}
    return render(request,"product/index.html",context)

def search(request):
    search_str = request.POST['search']
    pList = getLists('product_list.txt')
    searchList=[]
    for p in pList:
        if search_str in p[1]:
            searchList.append(p)
    context = {
        'search_str':search_str,
        'searchList':searchList
    }
    return render(request,"product/search.html",context)

