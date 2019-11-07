from django.db import models

# Create your models here.
class Figuras(models.Model):
	numero = models.IntegerField()

	def __str__(self):
		return self.numero