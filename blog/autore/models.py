from django.db import models
import datetime

# Create your models here.

class Autore(models.Model):
    nome = models.CharField(max_length=20, )
    cognome = models.CharField(max_length=20)
    nick = models.CharField(max_length=15, unique=True, help_text='Max 15 caratteri') #unico
    data_nascita = models.DateField() #anno/mese/giorno
    email = models.EmailField()
    password = models.CharField(max_length=20, help_text='Min 4 caratteri')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nome + " " + self.cognome + ", " + self.nick

    class Meta:
        get_latest_by  = ['-nome', '-cognome']
