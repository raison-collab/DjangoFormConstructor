from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    fields = models.ManyToManyField('Field', related_name='forms')

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('CharField', 'Текстовое поле'),
        ('EmailField', 'Поле для электронной почты'),
        ('IntegerField', 'Целочисленное поле'),
        # Добавить другие
    ])
    max_length = models.IntegerField(blank=True, null=True)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name
