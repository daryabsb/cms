from django import forms
from src.pages.models import Page, PageMeta, PageSeo


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = (
            'user_id',
            'parent',
            'type',
            'title',
            'slug',
            'excerpt',
            'content',
            'content2',
            'comment',
            'password',
            'status',
            'visibility',
            'password',
            'publish_on',
            'feature_image',
        )
        widgets = {
            'feature_image': forms.FileInput(),
        }


class PageMetaForm(forms.ModelForm):
    class Meta:
        model = PageMeta
        fields = (
            'name',
            'value',
        )


class PageSeoForm(forms.ModelForm):
    class Meta:
        model = PageSeo
        fields = (
            'title',
            'meta_keywords',
            'meta_descriptions',
        )
