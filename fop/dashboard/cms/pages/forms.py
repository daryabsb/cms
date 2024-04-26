from django import forms
from dashboard.cms.pages.models import Page, PageMeta, PageSeo
from ckeditor.widgets import CKEditorWidget

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
            'content': CKEditorWidget()
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
