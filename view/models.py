import uuid
from django.db import models
from metadata.models import Entity, Column
from django.utils.translation import gettext as _

class View(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    view = models.CharField(_('View name'),max_length=50, unique=True)
    isActive = models.BooleanField(_('Active'),default=False)
  
    def __str__(self):
        return '%s' % (self.view)

class EntityView(models.Model):
    options = (('main', 'Main'), ('secondary', 'Secondary'),('none','None'))

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    reference = models.CharField(max_length=10, default='main', choices=options)

    entity = models.ForeignKey(Entity, related_name="entityviewEntitys", blank=True, null=True, on_delete=models.CASCADE)
    view = models.ForeignKey(View, related_name="entityviewViews", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.view, self.entity)

class Dictionary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    dictionaryName = models.CharField(max_length=50, null=False, unique=False, default='')
    def __str__(self):
        return ' %s' % (self.dictionaryName)
        
class ColumnView(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    order = models.IntegerField(default=0)
    entityView = models.ForeignKey(EntityView, related_name="columnviewEntityView", blank=True, null=True, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, related_name="columnviewColumns", blank=True, null=True, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dictionary, related_name="columnviewDictionarys", blank=True, null=True, on_delete=models.CASCADE, default='None')
    isList = models.BooleanField(default=False)

    class Meta: 
        ordering = ['order','column']

    def __str__(self):
        return '(%s): %s' % (str(self.order), self.column)


class Filter(models.Model):
    options = (('=', '='), ('>', '>'), ('<', '<'), ('!=', '!='), ('<>', '<>'))

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    order = models.IntegerField(default=0)

    view = models.ForeignKey(View, related_name="filterViews", blank=True, null=True, on_delete=models.CASCADE)
    columnView = models.ForeignKey(ColumnView, related_name="filtercolumnViews", blank=True, null=True, on_delete=models.CASCADE)
    operator = models.CharField(max_length=2, default='=', choices=options)

    valor = models.CharField(max_length=25, default='', unique=False)

    class Meta:
        verbose_name = 'Condition Filter'
        verbose_name_plural = 'Condition Filters' 

    def __str__(self):
        return '%s: %s : %s : %s' % (str(self.order), self.columnView, self.operator, self.valor)
