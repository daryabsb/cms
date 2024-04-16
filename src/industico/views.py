from django.shortcuts import get_object_or_404, render
from src.blogs.models import Blogs

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


def index2(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/home/home-two.html"
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


def blog_classic(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_classic.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog",

    }
    return render(request, template_name, context)


def blog_detail(request, year, month, day, slug):

    print("Year is: ", year)

    blog = get_object_or_404(Blogs, slug=slug, publish_on__year=year, publish_on__month=month, publish_on__day=day)
    if not blog:
        blog = Blogs.objects.first()

    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_single.html"
    context = {
        "blog": blog,
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": blog.title,

    }
    return render(request, template_name, context)


def blog_detail_left_sidebar(request, year, month, day, slug):

    print("Year is: ", year)

    blog = get_object_or_404(Blogs, slug=slug, publish_on__year=year, publish_on__month=month, publish_on__day=day)
    if not blog:
        blog = Blogs.objects.first()

    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_single_left_sidebar.html"
    context = {
        "blog": blog,
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": blog.title,

    }
    return render(request, template_name, context)


def blog_detail_right_sidebar(request, year, month, day, slug):

    print("Year is: ", year)

    blog = get_object_or_404(Blogs, slug=slug, publish_on__year=year, publish_on__month=month, publish_on__day=day)
    if not blog:
        blog = Blogs.objects.first()

    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_single_right_sidebar.html"
    context = {
        "blog": blog,
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": blog.title,

    }
    return render(request, template_name, context)


def blog_grid(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_grid.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog Grid",

    }
    return render(request, template_name, context)


def blog_4_column(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog_grid_4.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog Grid 4 Column Full Width",

    }
    return render(request, template_name, context)

def blog_2_column(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog-grid-2.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog Grid Two Columns",

    }
    return render(request, template_name, context)


def blog_2_column_left_sidebar(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog-grid-2-column-left-sidebar.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog Grid Two Columns Left Sidebar",

    }
    return render(request, template_name, context)


def blog_2_column_right_sidebar(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/blog/blog-grid-2-column-right-sidebar.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Blog Grid Two Columns Right Sidebar",

    }
    return render(request, template_name, context)


# Projects


def project_2_column(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/2-columns-modern.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "2 Columns - Modern",

    }
    return render(request, template_name, context)


def project_3_column(request):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/3-columns-standard.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "3 Columns – Standard",

    }
    return render(request, template_name, context)


def project_4_column(request):

    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/4-columns-full-standard.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "4 Columns – Full Standard",

    }
    return render(request, template_name, context)


def project_4_column_grid(request):

    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/4-columns-full-grid.html"
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "4 Columns – Full Grid",

    }
    return render(request, template_name, context)


def project_portfolio(request, slug):
    # config_data = setup_config.loadConfig()
    # config_data.get('Theme', {}).get('value', 'theme5')
    theme_value = 'industico'
    template_name = f"{theme_value}/portfolio/project_details.html"
    print("Slug = ", slug)
    context = {
        "blogs": [],
        "banner_title": "Blogs",
        "query": 'query',
        "page_title": "Team Member",
        "page_title": "Oil Plant Project",
    }
    return render(request, template_name, context)

