from django.db import models

# Create your models here.


class Pupils(models.Model):
    name = models.CharField(max_length=50,verbose_name='Pupil name')
    image = models.IntegerField(verbose_name='Pupil age')
    mark1 = models.IntegerField(verbose_name='First month')
    mark2 = models.IntegerField(verbose_name='Second month')
    mark3 = models.IntegerField(verbose_name='Third month')
    mark4 = models.IntegerField(verbose_name='Fourth month')
    mark5 = models.IntegerField(verbose_name='Fifth month')
    mark6 = models.IntegerField(verbose_name='Sixth month')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pupils'
        verbose_name = 'Pupils list'
