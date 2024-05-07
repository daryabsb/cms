import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
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


# CRM VIEWS
@require_POST
def crm_menu_structure_save(request: HtmxHttpRequest) -> HttpResponse:

    order_no = 0

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
    # print("dd_data_list = ", dd_data_list)

    for dd_item_data in dd_data_list:
        item_obj = Items.objects.get(id=int(dd_item_data.get('id')))
    #     # Save ItemForm
        attributes = {}
        # item_obj.title = form_data_dict.get(f'item_label{item_obj.id}')

        title_attribute = form_data_dict.get(
            f'item_title_attribute{item_obj.id}')
        class_attribute = form_data_dict.get(
            f'item_class_attribute{item_obj.id}')
        target_attribute = form_data_dict.get(
            f'item_target_attribute{item_obj.id}')

        attributes["title"] = title_attribute
        attributes["class"] = class_attribute
        attributes["target"] = target_attribute

        item_obj.attributes = attributes

        item_obj.description = form_data_dict.get(
            f'item_description{item_obj.id}')
        item_url = form_data_dict.get(f'item_url{item_obj.id}')

        order_no += 1
        item_obj.order = order_no

        if item_url:
            item_obj.link = item_url

    #     # End ItemForm

        parent_id = dd_item_data.get('parent_id')
        if parent_id:
            parent_obj = Items.objects.get(id=int(parent_id))
            item_obj.parent = parent_obj
            item_obj.save()
        else:
            item_obj.parent = None
            item_obj.save()
    # End Save Menu Structure

    response = JsonResponse({"success": 'Menu  Update successfully'})

    response.status_code = 200
    return response
    # menu_items = Items.objects.filter(menu=menu_obj)
    # return render(
    #     request,
    #     'crm/cms/menu/partials/menu-nestable.html',
    #     {
    #         "done": "This is rendered!",
    #         "success": 'Menu  Update successfully',
    #         # "menu_obj": menu,
    #         "menu_items": menu_items,
    #         "menu_slug": menu_obj.slug
    #     },
    # )


@require_POST
def crm_update_menu_name(request, menu_id):

    menu_name = request.POST.get('menu_name', None)
    menu_obj = get_object_or_404(Menus, id=menu_id)
    menus = Menus.objects.all()

    if menu_name:
        menu_obj.title = menu_name
        menu_obj.save()

    context = {
        'menu_obj': menu_obj,
        'menus': menus,
    }
    return render(request, 'crm/cms/menu/renders/update_menu.html', context)


@require_GET
def crm_search_pages(request: HtmxHttpRequest) -> HttpResponse:
    from src.pages.models import Page
    search_keywords = request.GET.get("search_keywords", None)
    objects = []
    if search_keywords:
        objects = Page.objects.filter(title__icontains=search_keywords)

    return render(
        request,
        "crm/cms/menu/partials/left_search_results.html",
        {"objects": objects},
    )


@require_GET
def crm_search_blogs(request: HtmxHttpRequest) -> HttpResponse:
    from src.blogs.models import Blogs
    search_keywords = request.GET.get("search_keywords", None)
    objects = []
    if search_keywords:
        objects = Blogs.objects.filter(title__icontains=search_keywords)

    return render(
        request,
        "crm/cms/menu/partials/left_search_results.html",
        {"objects": objects},
    )


def crm_add_new_menu(request: HtmxHttpRequest) -> HttpResponse:
    menu_title = request.POST.get('menu_title')
    menu_link = request.POST.get('menu_link', '#')
    print(menu_title, menu_link)

    if menu_title:
        menu_obj = Menus(title=menu_title, user=request.user)
        menu_obj.link = menu_link
        menu_obj.save()

        response = JsonResponse({
            'title': 'Menu added',
            'message': "You successfully added a new menu, congrats!"
        })
        response.status_code = 200
    else:
        response = JsonResponse({
            'title': 'Menu failed',
            'message': "A title is essential in order to create a menu!"
        })
        response.status_code = 400

    return response


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items', 'menu.add_items'}, raise_exception=True)
@require_POST
def crm_add_menu_content(request: HtmxHttpRequest) -> HttpResponse:

    item_ids = request.POST.getlist('PageItem[]')
    menu_type = request.POST.get('menu_type')
    menu_id = request.POST.get('menu_id')
    menu_obj = Menus.objects.get(id=menu_id)
    allItems = []
    new_menu_item = {}

    print("Item IDs = ", item_ids)
    print("menu_type = ", menu_type)
    print("menu_obj = ", menu_obj)

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
                order=Items.objects.count() + 2

            )
            new_menu_item.save()
    menu_items = Items.objects.filter(menu=menu_obj)

    return render(
        request,
        'crm/cms/menu/partials/menu-nestable.html',
        {
            "new_menu_item": new_menu_item,
            "done": "This is rendered!",
            "menu_obj": menu_obj,
            "menu_items": menu_items,
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


@login_required(login_url='dashboard:login')
@permission_required({'menu.view_items', 'menu.add_items'}, raise_exception=True)
@require_POST
def crm_add_link_to_menu(request: HtmxHttpRequest) -> HttpResponse:
    menu_id = request.POST.get('menu_id')
    title = request.POST.get('linktitle').strip()
    link = request.POST.get('linkurl')

    print(f"Title={title} - Link= {link} - MenuID = {menu_id}")

    menu_obj = Menus.objects.get(id=request.POST.get('menu_id'))

    new_menu_item = Items(menu=menu_obj,
                          title=request.POST.get('linktitle').strip(),
                          type='Link',
                          attributes='{"title": "", "class": "", "target": ""}',
                          link=request.POST.get('linkurl')
                          )
    new_menu_item.save()

    if new_menu_item:
        response = JsonResponse({
            'title': 'Link To Menu Added',
            'message': "You successfully added a new link to menu, congrats!"
        })
        response.status_code = 200
    else:
        response = JsonResponse({
            'title': 'Link To Menu Failed',
            'message': "A title or link is essential in order to create a link!"
        })
        response.status_code = 400

    response.status_code = 200
    menu_items = Items.objects.filter(menu=menu_obj)
    # return response
    return render(
        request,
        'crm/cms/menu/renders/insert_menu.html',
        {
            "new_menu_item": new_menu_item,
            "done": "This is rendered!",
            "menu_obj": menu_obj,
            "menu_items": menu_items,
            "slug": menu_obj.slug,
            "success": True,
            'success_title': 'Link To Menu Added',
            'success_message': "You successfully added a new link to menu, congrats!"
        },
    )


@login_required(login_url='dashboard:login')
@permission_required({'auth.view_group'}, raise_exception=True)
def crm_groups_list(request):
    from django.contrib.auth.models import Group
    from django.db.models import Count
    context = {
        "groups": Group.objects.annotate(
            user_count=Count('user', distinct=True)).annotate(
                perms_count=Count('permissions', distinct=True)),
        "colors": {'primary': 'primary', 'success': 'success', 'dark': 'dark'},
        "page_title": "Groups"
    }

    return render(request, 'crm/accounts/groups/list.html', context)


@login_required(login_url='dashboard:login')
@permission_required({'auth.view_permission'}, raise_exception=True)
@require_GET
def crm_permissions_list(request):
    from django.contrib.auth.models import Permission
    from django.core.paginator import Paginator
    from src.accounts import utils

    permission_list = Permission.objects.all()
    # Show 5 permission per page.
    paginator = Paginator(permission_list, utils.nodes_per_page())

    page = int(request.GET.get('page', '1'))

    try:
        permissions = paginator.get_page(page)
    except:
        return HttpResponse('')

    context = {
        "permissions": permissions,
        "page": page,
        "page_title": "Permissions",
    }

    return render(request, 'crm/accounts/permissions/partials/loop-list.html', context)


# CMS VIEWS

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
    menu_slug = ''
    items = request.POST.getlist('item[]', [])
    menu_id = request.POST.get('menu_id', None)
    key2 = request.POST.get('key2', None)

    print("menu_id: ", menu_id)

    if menu_slug:
        menu = Menus.objects.get(id=menu_id)
    else:
        menu = Menus.objects.get(slug='mega-menu')

    all_items = Items.objects.filter(menu=menu).order_by('mptt_level')

    # Re-order items based on their position in the POST data
    order_count = 1
    for item_id in items:
        item = Items.objects.get(pk=item_id)
        if item.parent is None:  # Check if it's a top-level item
            item.order = order_count
            order_count += 1
        item.save()  # Save the updated order even for children (handled below)

    # Loop through all items again to fix child item ordering
    order_count = 1
    for item in all_items:
        if item.parent is not None:  # Skip top-level items
            parent_item = item.parent
            # siblings = list(Items.objects.filter(parent=parent_item).order_by('order'))  # Convert siblings to a list
            # item_position = siblings.index(item)  # Find position using index
            item.order = order_count  # Set order based on sibling position
            order_count += 1
            item.save()
    menu_items = Items.objects.filter(menu=menu)

    return render(
        request,
        'menu/menu_partials/menu_sortable.html',
        {
            "done": "This is rendered!",
            # "menu_obj": menu,
            "menu_items": menu_items,
            "menu_slug": menu.slug
        },
    )


@require_POST
def update_menu_name(request, menu_id):

    menu_name = request.POST.get('menu_name', None)
    menu_obj = get_object_or_404(Menus, id=menu_id)
    menus = Menus.objects.all()

    if menu_name:
        menu_obj.title = menu_name
        menu_obj.save()

    context = {
        'menu_obj': menu_obj,
        'menus': menus,
    }
    return render(request, 'menu/renders/update_menu.html', context)

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
