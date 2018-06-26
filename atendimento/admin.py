from django.contrib import admin
from atendimento.models import Atendimento
# Register your models here.

"""
class WebsiteAdmin(admin.ModelAdmin):
    model = Website

class LinkScriptHeadAdmin(admin.ModelAdmin):
    model = LinkScriptsHead

admin.site.register(Website, WebsiteAdmin, LinkScriptsHead)

"""

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    model = Atendimento

