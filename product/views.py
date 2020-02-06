from django.shortcuts import render
from product.functions import *

# Create your views here.

def index(request):
    pList = getLists('product_list.txt')
    context = {'pList':pList}
    return render(request,"product/index.html",context)


