from django import forms
from src.pages.models import Page, PageMeta, PageSeo
from ckeditor.widgets import CKEditorWidget
from django.conf.urls.static import static
class ContentWidget(CKEditorWidget):
  template_name = "dashboard/widgets/widget.html"
  class Media:
      css = {
          "all": ["pretty.css"],
      }
      js = [static('ckeditor/ckeditor/ckeditor.js')]

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
            'content': ContentWidget()
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
