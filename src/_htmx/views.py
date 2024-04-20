from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import (require_POST, require_GET,)
from django.contrib.auth.decorators import (login_required, permission_required,)

from django_htmx.middleware import HtmxDetails
from src._htmx.forms import SearchForm

# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails



@require_POST
def search_pages2(request: HtmxHttpRequest) -> HttpResponse:
    print("This view was called")
    form = SearchForm(request.POST)
    if form.is_valid():
        search_keywords = form.cleaned_data["search_keywords"]
    print("What is submitted? ", search_keywords)
    return render(
        request,
        "menu/menu_partials/left_search_results.html",
        {"form": form, "search_keywords": search_keywords},
    )

@require_GET
def search_pages(request: HtmxHttpRequest) -> HttpResponse:
    from src.pages.models import Page
    search_keywords = request.GET.get("search_keywords", None)
    objects = []
    if search_keywords:
        objects = Page.objects.filter(title__icontains=search_keywords)

    return render(
        request,
        "menu/menu_partials/left_search_results.html",
        {"objects": objects},
    )


@require_POST
def csrf_demo_checker(request: HtmxHttpRequest) -> HttpResponse:
    form = OddNumberForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data["number"]
        number_is_odd = number % 2 == 1
    else:
        number_is_odd = False
    return render(
        request,
        "csrf-demo-checker.html",
        {"form": form, "number_is_odd": number_is_odd},
    )


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items', 'menu.add_items'}, raise_exception=True)
def add_menu_content(request: HtmxHttpRequest) -> HttpResponse:
    from src.pages.models import Page
    from src.blogs.models import Blogs, Categories
    from src.menu.models import Menus, Items
    print("Adding new item!")

    if request.method == 'POST':
        item_ids = request.POST.getlist('MenuItem[]')
        menu_type = request.POST.get('menu_type')
        menu_id = request.POST.get('menu_id')
        menu_obj = Menus.objects.get(id=menu_id)
        allItems = []
        new_menu_item = {}
        if menu_type == 'Page':
            allItems = Page.objects.filter(id__in=item_ids)
            linkType = 'Page'

        if menu_type == 'Blog':
            allItems = Blogs.objects.filter(id__in=item_ids)
            linkType = 'Blog'

        if menu_type == 'Category':
            allItems = Categories.objects.filter(id__in=item_ids)
            linkType = 'Category'

        if allItems:
            for item_obj in allItems:
                new_menu_item = Items(
                    menu=menu_obj,
                    title=item_obj.title,
                    item_id=item_obj.id,  # item_id
                    type=linkType,

                )
                new_menu_item.save()
        return render(
        request,
        'menu/menu_partials/menu_nestable.html',
        {"new_menu_item": new_menu_item},
            )

