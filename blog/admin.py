from django.contrib import admin
from blog.models import Noticia
# Register your models here.

"""
class WebsiteAdmin(admin.ModelAdmin):
    model = Website

class LinkScriptHeadAdmin(admin.ModelAdmin):
    model = LinkScriptsHead

admin.site.register(Website, WebsiteAdmin, LinkScriptsHead)

"""

@admin.register(Noticia)
class BlogAdmin(admin.ModelAdmin):
    model = Noticia

