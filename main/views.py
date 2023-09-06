from django.shortcuts import render
from main.models import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all().values()
    context = {
        'items':items,
    }

    return render(request, "main.html", context)