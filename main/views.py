from django.shortcuts import render, redirect
from main.models import Item
from random import shuffle
from inventory.settings import BASE_DIR, ALLOWED_FILES, STATIC_URL
import json

# Create your views here.
def show_main(request):
    # Grab items from database
    items = Item.objects.all()

    # generate 5 random integers from 1-len(items)
    # this is the id's of the items chosen
    indexes = [i for i in range(1, len(items)+1)]
    shuffle(indexes)
    indexes = indexes[:5]
    
    # filter only the id's chosen, then order by rarity (asc.) and name
    items = items.filter(id__in=indexes).order_by('-rarity', 'name').values()
    
    context = {
        'items': items,
    }

    return render(request, "main.html", context)

def show_landing(request):
    with open(BASE_DIR/'README.md', 'rb') as f:
        a = f.read().decode()   
    context = {
        'content': a
    }
    return render(request, "md.html", context)

def show_media(request):
    statics = json.loads(open(BASE_DIR/'static/staticfiles.json', "r").read())['paths']
    fstr = "main" + request.path
    
    if fstr not in statics:
        fstr = "main/media/tricksnack.gif"
        print("bad")

    context = {
        'furl' : fstr
    }
    
    print(STATIC_URL + fstr)
    return render(request, "image.html", context)