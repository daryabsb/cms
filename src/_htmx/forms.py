from __future__ import annotations

from django import forms


class SearchForm(forms.Form):
    search_keywords = forms.CharField()