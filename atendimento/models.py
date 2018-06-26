from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Atendimento(models.Model):
	
	paciente = models.ForeignKey(
						User, 
						verbose_name="Selecione o Paciente",
                        on_delete=models.CASCADE,
                        )

	data_cadastro = models.DateTimeField(
            blank=True, null=True, default=timezone.now)


	def __str__(self):
		return self.paciente.username