from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm



def about(request):
    return render(request, "coore/about.html")

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, "coore/index.html", {
        'categories': categories,
        'items': items, 
    })

def contact(request):
    return render(request, "coore/contact.html")


def logout(request):
    return redirect('/login/')




def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm() 
    form = SignupForm()

    return render(request, 'coore/signup.html',{
        'form': form
    })