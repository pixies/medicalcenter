from django.db import models
from django.utils.translation import ugettext_lazy as _

from endereco.models import Address

from .constants import (
    GENERO,
    ESTADO_CIVIL,
)

# Create your models here.
class Profile(models.Model):


    primeiro_nome = models.CharField(_('Primeiro nome'), max_length=255, blank=True)
    segundo_nome = models.CharField(_('Segundo nome'), max_length=255, blank=True)
    phone_cell = models.CharField(_('Celular'), max_length=30, blank=True)

    data_nascimento = models.DateField(_("Data de nascimento"), blank=False)

    genero = models.CharField(_('Genero'), max_length=50, blank=False, choices=GENERO)

    estado_civil = models.CharField(_('Genero'), max_length=50, blank=False, choices=ESTADO_CIVIL)

    naturalidade = models.CharField(_('Naturalidade'), max_length=255, blank=False)

    email = models.EmailField(_('E-mail'), max_length=255, blank=False)
    celular = models.CharField(_('Celular'), max_length=255, blank=False)
    fone = models.CharField(_('Telefone Fixo'), max_length=255, blank=False)
    #status = models.BooleanField(default=False, verbose_name=_("I want to support"))

    #dados complementares
    cpf = models.CharField(_('CPF'), max_length=255, blank=True)
    rg = models.CharField(_('RG'), max_length=255, blank=True)
    emissor = models.CharField(_('Orgão emissor'), max_length=255, blank=True)
    profissao = models.CharField(_('Profissão'), max_length=255, blank=True)
    empresa = models.CharField(_('Empresa'), max_length=255, blank=True)
    peso = models.CharField(_('Peso'), max_length=255, blank=True)
    altura = models.CharField(_('Altura'), max_length=255, blank=True)


    #endereco
    endereco = models.ForeignKey(Address, _('Endereço'), blank=False)

    #dados familiares
    nome_mae = models.CharField(_('Nome da Mãe'), max_length=255, blank=False)
    nome_pai = models.CharField(_('Nome do Pai'), max_length=255, blank=False)
    nome_responsavel = models.CharField(_('Nome do Responsável'), max_length=255, blank=False)

    #outros
    alergias = models.TextField(_('Alergias?'), max_length=255, blank=False)
    observacoes = models.TextField(_('Observações'), max_length=255, blank=False)

    #convenios
    convenio = models.CharField(_('Convênio'), max_length=255, blank=False)
    numero_carteira = models.CharField(_('Número da Carteira'), max_length=255, blank=False)
    validade = models.CharField(_('Validade'), max_length=255, blank=False)