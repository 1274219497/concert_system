# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Concert(models.Model):
    name = models.CharField(unique=True, max_length=100)
    remain_seat = models.IntegerField()
    total_seat = models.IntegerField()
    time = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    singer = models.OneToOneField('Singer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'concert'


class Fan(models.Model):
    cardid = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    is_select = models.CharField(max_length=1)
    account = models.IntegerField()
    user = models.OneToOneField('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fan'


class FanTicket(models.Model):
    fan = models.ForeignKey(Fan, models.DO_NOTHING)
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fan_ticket'


class Node(models.Model):
    function_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'node'


class Role(models.Model):
    rolename = models.CharField(unique=True, max_length=100)
    level = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'role'


class RoleNode(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    node = models.ForeignKey(Node, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_node'


class Singer(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'singer'


class Ticket(models.Model):
    name = models.CharField(unique=True, max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=1)
    remain = models.IntegerField()
    total = models.IntegerField()
    concert = models.ForeignKey(Concert, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket'


class User(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'
