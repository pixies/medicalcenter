from django.db import models
from django.utils import timezone

from atendimento.models import Atendimento

# Create your models here.
class Exame(models.Model):

	atendimento = models.ForeignKey(
						Atendimento, 
						verbose_name="Atendimento",
                        on_delete=models.CASCADE,
                        )

	tipo_exame = models.CharField(verbose_name="Nome do Exame", max_length=200)
	
	descricao = models.TextField(verbose_name="Descrição do Exame")

	exame = models.FileField(upload_to='file_exames/%Y/%m/%d/')

	data_entrega = models.DateTimeField(
            blank=True, null=True, default=timezone.now)


	def __str__(self):
		return self.tipo_exame