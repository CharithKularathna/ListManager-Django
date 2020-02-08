from django.shortcuts import render
from product.functions import *

# Create your views here.
FILE_PATH = 'product_list.txt'

def index(request):
    pList = getLists(FILE_PATH)
    context = {'pList':pList}
    return render(request,"product/index.html",context)

def search(request):
    search_str = request.POST['search']
    pList = getLists(FILE_PATH)
    searchList=[]
    for p in pList:
        if search_str in p[1]:
            searchList.append(p)
    context = {
        'search_str':search_str,
        'searchList':searchList
    }
    return render(request,"product/search.html",context)

def add(request):
    return render(request,"product/add.html")

def addResult(request):
    product_id = request.POST['product_id']
    product_name = request.POST['product_name']
    price = request.POST['price']
    try:
        if (price[0]=="$"):
            float(price[1:])
        else:
            float(price)
    except ValueError:
        context = {
            'result':0
        }
        return render(request,"product/addResult.html",context)
    else:
        if (price[0]!="$"):
            price = "$"+ price
        context = {
            'result':1
        }
        writeList = [product_id, product_name, price]
        addProduct(FILE_PATH,writeList)
        return render(request,"product/addResult.html",context)

def removeResult(request):
    product_id = request.POST['product_id']
    result = removeProduct(FILE_PATH,product_id)
    context = {
        'product_id':product_id,
        'result':result
    }
    return render(request,"product/removeResult.html",context)

def remove(request):
    return render(request,"product/remove.html")