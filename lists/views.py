from django.utils.html import escape
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    item = Item(text=new_item_text, list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        response = render(request, 'lists/home.html', {'error': error})
        return response
    return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
    list = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list})

def home_page(request):
    return render(request, 'lists/home.html')
