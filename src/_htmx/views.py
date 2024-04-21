import json
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import (require_POST, require_GET,)
from django.contrib.auth.decorators import (
    login_required, permission_required,)

from django_htmx.middleware import HtmxDetails
from src._htmx.forms import SearchForm

from django.http import JsonResponse

from src.pages.models import Page
from src.blogs.models import Blogs, Categories
from src.menu.models import Menus, Items

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
@require_POST
def add_menu_content(request: HtmxHttpRequest) -> HttpResponse:


    item_ids = request.POST.getlist('MenuItem[]')
    menu_type = request.POST.get('menu_type')
    menu_id = request.POST.get('menu_id')
    menu_obj = Menus.objects.get(id=menu_id)
    allItems = []
    new_menu_item = {}

    print("Item IDs = ", item_ids)
    print("menu_type = ", menu_type)
    print("menu_obj = ", menu_obj)

    if item_ids:
        allItems = Page.objects.filter(id__in=item_ids)
        linkType = 'Page'

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
        {
            "new_menu_item": new_menu_item,
            "done": "This is rendered!",
            "menu_obj": menu_obj,
            "slug": menu_obj.slug
        },
    )

    # if menu_type == 'Page':
    #     allItems = Page.objects.filter(id__in=item_ids)
    #     linkType = 'Page'

    # if menu_type == 'Blog':
    #     allItems = Blogs.objects.filter(id__in=item_ids)
    #     linkType = 'Blog'

    # if menu_type == 'Category':
    #     allItems = Categories.objects.filter(id__in=item_ids)
    #     linkType = 'Category'



# @login_required(login_url='dashboard:login')
# @permission_required({'menu.view_menus','menu.view_items','menu.change_menus','menu.change_items'}, raise_exception=True)
@require_POST
def cms_menu_structure_save(request: HtmxHttpRequest) -> HttpResponse:

    items = request.POST.getlist('item[]', [])
    menu_slug = request.POST.get('menu_data', None)
    
    order_no=0
    menu = Menus.objects.get(slug=menu_slug)
    for item in items:
        print("Current item is: ", item)
        menu_item = Items.objects.filter(menu=menu, id=item).first()
        if menu_item:
            menu_item.order = order_no + 1
            menu_item.save()


    '''

    form_data_dict = {}
    form_data_list = json.loads(request.POST.get('form_data'))
    for field in form_data_list:
        form_data_dict[field["name"]] = field["value"]
        

    # Start Save Menu Structure
    


    dd_data_list = json.loads(request.POST.get('dd_data'))
    menu_data = json.loads(request.POST.get('menu_data'))


    menu_obj = Menus.objects.get(id=menu_data.get('menu_id'))

   

    menu_obj.title = menu_data.get('menu_name')
    menu_obj.save()
    

    for dd_item_data in dd_data_list:
        item_obj = Items.objects.get(id=int(dd_item_data.get('id')))
        #Save ItemForm
        attributes={}
        item_obj.title = form_data_dict.get(f'item_label{item_obj.id}')
        
        
        title_attribute =  form_data_dict.get(f'item_title_attribute{item_obj.id}')
        class_attribute =  form_data_dict.get(f'item_class_attribute{item_obj.id}')
        target_attribute =  form_data_dict.get(f'item_target_attribute{item_obj.id}')
        
        attributes["title"]=title_attribute
        attributes["class"]=class_attribute
        attributes["target"]=target_attribute

                
        item_obj.attributes = attributes
    
        item_obj.description = form_data_dict.get(f'item_description{item_obj.id}')
        item_url = form_data_dict.get(f'item_url{item_obj.id}')
        
        order_no += 1
        item_obj.order=order_no
        

        if item_url:
            item_obj.link = item_url

        #End ItemForm


        parent_id = dd_item_data.get('parent_id')
        if parent_id:
            parent_obj = Items.objects.get(id=int(parent_id))
            item_obj.parent = parent_obj
            item_obj.save()
        else:
            item_obj.parent = None
            item_obj.save()
    #End Save Menu Structure

    response = JsonResponse({"success": 'Menu  Update successfully'})

    '''
    return render(
        request,
        'menu/menu_partials/menu_sortable.html',
        {
            "done": "This is rendered!",
            "menu_obj": menu,
            "slug": menu.slug
        },
    )