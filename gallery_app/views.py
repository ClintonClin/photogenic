from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category, Image


def main(request):
    all_images = Image.objects.all()
    categories = Category.objects.all()
    title = 'Home'

    return render(request, 'index.html', {'all_images': all_images, 'categories': categories, 'title': title})


def search_results(request):
    categories = Category.objects.all()
    title = 'Search'

    if 'searchcat' in request.GET and request.GET["searchcat"]:
        search_term = request.GET.get("searchcat")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html', {"message": message, "all_images": searched_images, 'categories': categories, 'title': title})

    else:
        message = "No search item."
        return render(request, 'index.html', {"message": message, 'categories': categories, 'title': title})


def page_category(request, category):
    categories = Category.objects.all()
    title = f"{category}"
    category_results = Image.search_category(category)
    return render(request, 'index.html', {'all_images': category_results, 'categories': categories, 'title': title})



