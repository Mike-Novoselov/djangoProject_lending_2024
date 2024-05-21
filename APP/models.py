from django.db import models

# формирую таблицу для б\д.

class Client(models.Model):
    name = models.CharField(verbose_name='Ф.И.О', max_length=30)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    email = models.EmailField(verbose_name='email', unique=True)

    def __str__(self):
        return self.name

"""
python manage.py makemigrations
python manage.py migrate
"""