from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect('/lists/the-only-list-in-the-world/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})

def home_page(request):
    return render(request, 'lists/home.html')
