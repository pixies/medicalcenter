from django.contrib import admin
from exame.models import Exame
# Register your models here.

"""
class WebsiteAdmin(admin.ModelAdmin):
    model = Website

class LinkScriptHeadAdmin(admin.ModelAdmin):
    model = LinkScriptsHead

admin.site.register(Website, WebsiteAdmin, LinkScriptsHead)

"""

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    model = Exame

