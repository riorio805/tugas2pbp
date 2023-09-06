from django.shortcuts import render, redirect
from main.models import Item
from random import shuffle

# Create your views here.
def show_main(request):
    # Grab items from database
    items = Item.objects.all()

    # generate 5 random integers from 1-len(items)
    # this is the id's of the items chosen
    indexes = [i for i in range(1, len(items)+1)]
    shuffle(indexes)
    
    # filter only the id's chosen, then order by rarity (asc.) and name
    items = items.filter(id__in=indexes).order_by('-rarity', 'name').values()
    
    context = {
        'items': items,
    }

    return render(request, "main.html", context)


def redirect_main(request):
    response = redirect('/main/')
    return response