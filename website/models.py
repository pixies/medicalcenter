from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()

# Create your models here.
class LinkScriptsHead(models.Model):
    """
        LinkScript Model
        <link href="{% static 'css/materialize.css' %}" type="text/css" rel="stylesheet" media="screen,projection"/>
    """

    script_name = models.CharField(verbose_name=_('Nome usado para identificar o script'), max_length=1000, blank=True)
    href = models.CharField(verbose_name=_('Caminho do Script'), max_length=1000, blank=True)
    type = models.CharField(verbose_name=_('Tipo de script'), max_length=1000, blank=True)
    rel = models.CharField(verbose_name=_('Rel'), max_length=1000, blank=True)
    #media = models.CharField(verbose_name=_('Caminho do Script'), max_length=1000, blank=True)

    class Meta:
        verbose_name = _('Scripts do cabeçalho')
        verbose_name_plural = _('Scripts do cabeçalho')

    def __str__(self):
        return str(self.script_name)

class Website(models.Model):
    """
        Header Model
        ------------
        <head>
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
          <meta name="viewport" content="width=device-width, initial-scale=1"/>
          <title>Parallax Template - Materialize</title>

          <!-- CSS  -->
          <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
          <link rel="stylesheet" href="http://cdn.materialdesignicons.com/2.2.43/css/materialdesignicons.min.css" crossorigin="anonymous">

          <link href="{% static 'css/materialize.css' %}" type="text/css" rel="stylesheet" media="screen,projection"/>
          <link href="{% static 'css/style.css' %}" type="text/css" rel="stylesheet" media="screen,projection"/>
        </head>

    """
    usuario = models.ForeignKey(User, verbose_name=_('User name'), on_delete=True)
    title = models.CharField(verbose_name=_('Título'), max_length=400)
    list_scripts = models.ManyToManyField(LinkScriptsHead, verbose_name=_('Scripts'), blank=True)

    class Meta:
        verbose_name = _('Website')
        verbose_name_plural = _('Websites')

    def __str__(self):
        return str(self.title)
