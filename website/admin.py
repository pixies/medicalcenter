from django.contrib import admin
from website.models import Website, LinkScriptsHead
# Register your models here.

"""
class WebsiteAdmin(admin.ModelAdmin):
    model = Website

class LinkScriptHeadAdmin(admin.ModelAdmin):
    model = LinkScriptsHead

admin.site.register(Website, WebsiteAdmin, LinkScriptsHead)

"""

@admin.register(Website, LinkScriptsHead)
class WebsiteAdmin(admin.ModelAdmin):
    model = Website
