from django.contrib import admin
from src.reels.models import Video
from mptt.admin import MPTTModelAdmin


admin.site.register(Video,MPTTModelAdmin)