# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import timedelta

import datetime

import time
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DecimalField, CharField, IntegerField, BooleanField, TextField, URLField, \
    BigIntegerField
from django.db.models.fields.related import ForeignKey, OneToOneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = CharField(verbose_name='Telefone principal', default='', max_length=20)
    phoneSecondary = CharField(verbose_name='Telefone secundário', default='', max_length=20)

    facebook = URLField(verbose_name='Link para o facebook', default='')

    def __str__(self):
        return self.user.get_full_name()


class Home(models.Model):
    user = ForeignKey(User, verbose_name='Responsável', on_delete=models.CASCADE, related_name='houses')
    latitude = DecimalField(default=0, max_digits=30, decimal_places=20)
    longitude = DecimalField(default=0, max_digits=30, decimal_places=20)

    HOME_TYPES = (
        ('HOUSE', 'Casa'),
        ('APARTAMENT', 'Apartamento')
    )
    type = CharField(verbose_name='Tipo de moradia', max_length=255, choices=HOME_TYPES, default='HOUSE')
    
    building = CharField(verbose_name='Nome do prédio', default='', max_length=255)
    residents = IntegerField('Número de moradores', default=1)
    apartment = IntegerField(verbose_name='Número do apartamento', default=0)
    internet = BooleanField(verbose_name='Tem internet', default=True)
    internetPrice = DecimalField(verbose_name='Mensalidade da internet', default=0, max_digits=20, decimal_places=2)
    rooms = IntegerField(verbose_name='Número de quartos', default=2)
    price = DecimalField(verbose_name='Valor do aluguel', default=0, max_digits=20, decimal_places=2)
    comment = TextField(verbose_name='Comentários', max_length=1024 * 1024)


class Offer(models.Model):
    user = ForeignKey(User, verbose_name='Responsável', on_delete=models.CASCADE, related_name='offers')
    home = OneToOneField(Home, verbose_name='Moradia', on_delete=models.CASCADE, related_name='offer')
    vacancies = IntegerField('Número de vagas', default=1)

    active = BooleanField(verbose_name='Ativo', default=True)
    begin = BigIntegerField(verbose_name='Data de início do anúncio', default=0)
    end = BigIntegerField(verbose_name='Data de término do anúncio', default=0)

    def isActive(self):
        # Está ativo e o fim do anúncio ainda não chegou
        return self.active and datetime.datetime.now() < datetime.datetime.fromtimestamp(self.end)

    def renew(self, days):
        date = (datetime.datetime.fromtimestamp(self.end) + timedelta(days=days))
        self.end = int(time.mktime(date.timetuple()))
