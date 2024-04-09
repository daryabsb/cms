from django.shortcuts import render

# Create your views here.


def index(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/home/index.html"
    # config = setup_config.loadConfig()
    # query = request.GET.get('search')
    # if config['Reading']['show_on_front']['value'] == 'Page':
    #     if query:
    #         render_data = blog_list(request)
    #     else:
    #         render_data = page_detail(request)
    # if config['Reading']['show_on_front']['value'] == 'Blog':
    #     render_data = blog_list(request)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query'
    }
    return render(request, template_name, context)


def index3(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/home/home-three.html"
    # config = setup_config.loadConfig()
    # query = request.GET.get('search')
    # if config['Reading']['show_on_front']['value'] == 'Page':
    #     if query:
    #         render_data = blog_list(request)
    #     else:
    #         render_data = page_detail(request)
    # if config['Reading']['show_on_front']['value'] == 'Blog':
    #     render_data = blog_list(request)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query'
    }
    return render(request, template_name, context)
