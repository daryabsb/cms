from django import forms
from src.blogs.models import Categories, Blogs, Tags, Metas, Seo
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django_select2.forms import Select2Widget


class BlogForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'name':'blog_title1'}))

    class Meta:
        model = Blogs
        fields = (
            'title',
            'slug',
            'content2',
            'excerpt',
            'tags',
            'comment',
            'password',
            'status',
            'visibility',
            'publish_on',
            'feature_image',
            'video_url',
            'user'
        )
        widgets = {
            'feature_image': forms.FileInput(),
            # 'tags': Select2Widget(),
        }


class MetaForm(forms.ModelForm):
    class Meta:
        model = Metas
        fields = (
            'title',
            'value',
        )


class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo
        fields = (
            'title',
            'meta_keywords',
            'meta_descriptions',

        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = (
            'name',
        )


class CategoriesForm(forms.ModelForm):

    parent = TreeNodeChoiceField(
        queryset=Categories.objects.all(), level_indicator='+--', required=False)

    class Meta:
        model = Categories
        fields = ('title', 'parent')
