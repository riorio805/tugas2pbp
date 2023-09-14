from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.models import Item
from main.forms import ItemForm
from inventory.settings import BASE_DIR, ALLOWED_FILES, STATIC_URL, STATIC_ROOT
from random import shuffle
import json

# Create your views here.
def show_main(request, item_count=0):
    # Grab items from database
    items = Item.objects.all()
    all_item_count = len(items)

    # randomly select n items if item_count > 0
    indexes = [i for i in range(1, len(items)+1)]
    if item_count > 0:
        shuffle(indexes)
        indexes = indexes[:item_count]
    
    # filter only the id's chosen, then order by rarity (asc.) and name
    items = items.filter(id__in=indexes).order_by('rarity', 'name').values()
    
    # process rarity into a string
    # ★☆
    rarity = {}
    for i in items:
        rarity[i['id']] = "★" * i['rarity'] + "☆" * (5 - i['rarity'])


    context = {
        'items': items,
        'all_item_count': all_item_count,
        'item_count': len(items),
        'rarity': rarity,
    }

    return render(request, "main.html", context)


def show_readme(request):
    with open(BASE_DIR/'README.md', 'rb') as f:
        a = f.read().decode()   
    context = {
        'content': a
    }
    return render(request, "md.html", context)


def show_archive(request, file):
    file = 'archive/' + file
    print(file)
    with open(BASE_DIR / file , 'rb') as f:
        a = f.read().decode()   
    
    context = {
        'content': a
    }
    return render(request, "md.html", context)


def show_statics_list(request):
    statics = json.loads(open(STATIC_ROOT/'staticfiles.json', "r").read())['paths']
    static_list = ['/'.join(i.split('/')[1:]) for i in statics if (i[:5]=="main/")]
    
    context = {
        'static_list': static_list
    }
    return render(request, "statics_list.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")