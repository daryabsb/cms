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
        "query": 'query',
        "page_title": "Home Page 1"
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


def about2(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/about-us-2.html"
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
        "query": 'query',
        "page_title": "About Us 2"
    }
    return render(request, template_name, context)


def about1(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/about-us-1.html"

    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "About Us 1"
    }
    return render(request, template_name, context)


def services1(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/services-1.html"

    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Services 1"
    }
    return render(request, template_name, context)


def services2(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/services-2.html"

    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Services Two"
    }
    return render(request, template_name, context)


def our_team(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/our-team.html"

    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Our Team"
    }
    return render(request, template_name, context)


def contact_us(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/contact-us.html"

    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Contact Us"
    }
    return render(request, template_name, context)


def team_member(request, slug):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/team-member.html"
    print("Slug = ", slug)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Team Member",
        "object": {"name": "Darya Ibrahim"},
    }
    return render(request, template_name, context)


def faq(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/pages/faq.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "FAQ",

    }
    return render(request, template_name, context)

def service_detail_left(request, slug):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/service/detail-left-sidebar.html"
    title = ' '.join([word.capitalize() for word in slug.split('-')])
    print("Slug = ", title)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Team Member",
        "object": {"title": title},
    }
    return render(request, template_name, context)

def service_detail_right(request, slug):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/service/detail-right-sidebar.html"
    title = ' '.join([word.capitalize() for word in slug.split('-')])
    print("Slug = ", title)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Team Member",
        "object": {"title": title},
    }
    return render(request, template_name, context)


def service_detail(request, slug):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/service/detail-no-sidebar.html"
    title = ' '.join([word.capitalize() for word in slug.split('-')])
    print("Slug = ", title)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Team Member",
        "object": {"title": title},
    }
    return render(request, template_name, context)