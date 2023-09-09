from django.shortcuts import render, redirect
from main.models import Item
from random import shuffle
from inventory.settings import BASE_DIR, ALLOWED_FILES, STATIC_URL

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
    fstr = request.path.split('/')[-1].split('.')
    fstr = fstr[0] + '.' + fstr[-1]
    ftype = fstr.split('.')[-1]
    if ftype not in ALLOWED_FILES:
        fstr = "tricksnack.gif"
        print("bad")
    
    fstr = "main/media/" + fstr
    context = {
        'furl' : fstr
    }
    
    print(STATIC_URL + fstr)
    return render(request, "image.html", context)