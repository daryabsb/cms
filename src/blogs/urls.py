from django.urls import path
from src.blogs.views import (
    cms_blog_list, cms_blog_delete, cms_blog_create, cms_blog_add_category,
    cms_blog_edit, delete_multiple_blogs, blogCategory, blogCategoryDelete,
    blogCategoryEdit, blogTag, blogTagEdit, blogTagDelete,
    crm_blog_list, crm_blog_create, crm_blog_edit,
    crm_blog_category, crm_blog_category_edit, crm_blog_category_add, crm_blog_category_delete,
    # cms_blog_custom_field_delete,
)


app_name = 'blog'
urlpatterns = [
    path('', cms_blog_list, name='blogs'),
    path('create/', cms_blog_create, name='blog_create'),
    path('edit/<int:id>', cms_blog_edit, name='blog_edit'),
    path('blog_delete/<int:id>/', cms_blog_delete, name='blog_delete'),
    path('blog_category_add/', cms_blog_add_category, name='blog_category_add'),
    # path('blog_custom_field_delete/<int:id>/',cms_blog_custom_field_delete, name="blog_custom_field_delete"),
    path('delete-multiple-blogs/', delete_multiple_blogs,
         name='delete-multiple-blogs'),

    path('categories/', blogCategory, name='blogCategory'),
    path('blog-category-delete/<int:id>/',
         blogCategoryDelete, name='blogCategoryDelete'),
    path('blog-category-edit/<int:id>/',
         blogCategoryEdit, name='blogCategoryEdit'),

    path('tags/', blogTag, name='blogTag'),
    path('tag-edit/<int:id>/', blogTagEdit, name='blogTagEdit'),
    path('tag-delete/<int:id>/', blogTagDelete, name='blogTagDelete'),

    # CRM URLS
    path('list/', crm_blog_list, name='blogs-list'),
    path('add/', crm_blog_create, name='blogs-add'),
    path('edit/<int:id>/', crm_blog_edit, name='blog-edit'),

    path('category/', crm_blog_category, name='blog-category'),
    path('category-edit/<int:id>/', crm_blog_category_edit,
         name='blog-category-edit'),
    path('category-edit/<int:id>/', crm_blog_category_edit,
         name='blog-category-edit'),
    path('category-add/', crm_blog_category_add,
         name='blog-category-add'),
    path('category-delete/<int:id>/', crm_blog_category_delete,
         name='blog-category-delete'),

]
