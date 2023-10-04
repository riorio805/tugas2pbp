from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.models import Item
from main.forms import ItemForm
from inventory.settings import BASE_DIR, ALLOWED_FILES, STATIC_URL, STATIC_ROOT
from random import shuffle
import json
import os
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request, item_count=-1):
    # Grab items from database
    items = Item.objects.all()
    all_item_count = len(items)
    user_item_count = len(Item.objects.filter(created_by=request.user))

    # randomly select n items from database if item_count >= 0
    indexes = [i.pk for i in items]
    if item_count >= 0:
        shuffle(indexes)
        indexes = indexes[:item_count]
        # filter only the id's chosen, then order by rarity (asc.) and name
        items = items.filter(id__in=indexes)

    items = items.order_by('rarity', 'name')
    
    # process rarity into a string
    # ★☆
    rarity = {}
    for i in items:
        rarity[i.pk] = "★" * i.rarity + "☆" * (5 - i.rarity)
    
    if items:
        last_item = items[len(items)-1].pk
    else:
        last_item = -1

    context = {
        'items': items,
        'all_item_count': all_item_count,
        'user_item_count': user_item_count,
        'item_count': len(items),
        'rarity': rarity,
        'name': request.user.username,
        'last_item': last_item,
    }

    if 'last_login' in request.COOKIES:
        context['last_login'] = request.COOKIES['last_login']

    return render(request, "main.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()), max_age=10000)
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response




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
    statics = json.loads(open(os.path.join(STATIC_ROOT, 'staticfiles.json'), "r").read())['paths']
    static_list = {}

    for i in statics:
        # check static location
        sdir = i.split('/')[0]
        # if admin get out
        if sdir == "admin": continue
        if sdir not in static_list:
            static_list[sdir] = []
        static_list[sdir].append('/'.join(i.split('/')[1:]))

    context = {
        'static_list': static_list
    }
    return render(request, "statics_list.html", context)


@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None, initial={'rarity': 3})

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)


@login_required(login_url='/login')
def change_item(request, id, amount=1):
    items = Item.objects.filter(pk=id)

    if len(items) == 0:
        messages.info(request, 'Item does not exist.')
        return HttpResponseRedirect(reverse('main:show_main'))

    item = items[0]

    if item.amount == 0:
        messages.info(request, 'Cannot decrease amount any further.')
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        item.amount += amount
        item.save()
        
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def delete_item(request, id):
    items = Item.objects.filter(pk=id)

    if len(items) == 0:
        messages.info(request, 'Item does not exist.')
        return HttpResponseRedirect(reverse('main:show_main'))

    item = items[0]
    
    if item.created_by == request.user:
        item.delete()
        messages.success(request, 'Successfully deleted item.')
    else:
        messages.info(request, 'Item can only be deleted by creator.')
    

    return HttpResponseRedirect(reverse('main:show_main'))


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