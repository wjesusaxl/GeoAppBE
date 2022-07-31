import uuid
from django.db import models

# Create your models here.
class EntityType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    entityTypeName = models.CharField(max_length=25, null=False, unique=False, default='')

    class Meta:
        verbose_name = 'EntityType'
        verbose_name_plural = 'EntityTypes' 

    def __str__(self):
        return self.entityTypeName

# Create your models here.
class Constraint(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    constraintName = models.CharField(max_length=50, null=False, unique=False, default='')
    constraintCode = models.CharField(max_length=5000, null=False, unique=False, default='')

    class Meta:
        verbose_name = 'Constraint'
        verbose_name_plural = 'Constraints' 

    def __str__(self):
        return self.constraintName
    
class DataType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    dataType = models.CharField(max_length=25, null=False, unique=True, default='')
    dataTypeCsd = models.CharField(max_length=25, null=False, unique=False, default='')

    class Meta:
        verbose_name = 'DataType'
        verbose_name_plural = 'DataTypes' 

    def __str__(self):
        return self.dataType 

class Entity(models.Model):
    options = (('main', 'Main'), ('secondary', 'Secondary'), ('none','None'))

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    entityName = models.CharField(max_length=50, unique=True, blank=False)
    entityLabel = models.CharField(max_length=50, unique=True, blank=False, default='')
    entityLabelCsd = models.CharField(max_length=50, unique=True, blank=False, default='')
    description = models.CharField(max_length=250)

    reference = models.CharField(max_length=10, default='main', choices=options)

    constraint = models.ForeignKey(Constraint, related_name="constraint_entity", blank=True, null=True, on_delete=models.CASCADE)
    entityType = models.ForeignKey(EntityType, related_name="entitytype_entity", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities' 

    def __str__(self):
        return '%s' % (self.entityName)

class Rule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    ruleName = models.CharField(max_length=100, null=False, unique=True, default='')
    ruleCode = models.CharField(max_length=5000, null=False, unique=False, default='')

    dataType = models.ForeignKey(DataType, related_name="datatype_rule", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules' 

    def __str__(self):
        return self.ruleName

class Column(models.Model):
    options = (('primarykey', 'PrimaryKey'), ('foreignkey', 'ForeignKey'), ('none', 'None'))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    order = models.IntegerField(default=0)
    columnName = models.CharField(db_index=True, unique=False, max_length=254)
    columnNameCsd = models.CharField(db_index=True, unique=False, max_length=254, default='')
    columnLabel = models.CharField(max_length=50, null=False, unique=False, default='')
    description = models.CharField(max_length=255, null=False, unique=False, default='')
    sourceCsd = models.CharField(max_length=255, null=False, unique=False, default='')
    lenght = models.IntegerField(blank=False, null=False)
    relationType = models.CharField(max_length=25, default='none', choices=options)
    isVisible = models.BooleanField(default=False) 
    isRequired  = models.BooleanField(default=False)
    isReadOnly  = models.BooleanField(default=False)
    isAppField = models.BooleanField(default=False)
    IsCustom = models.BooleanField(default=False)
    IsUnique  = models.BooleanField(default=False)
    MultValues = models.CharField(max_length=1000, null=False, unique=False, default='')
    IsCustom  = models.BooleanField(default=False)
    IsIdentifier = models.BooleanField(default=False)
    IsMandatory = models.BooleanField(default=False)

  #ExtEntityData varchar(100)  DEFAULT NULL,
  #ExtFieldRel varchar(50)  DEFAULT NULL,
  #IsVisibleExt tinyint(4) DEFAULT NULL,
  #IsExtLabel tinyint(4) DEFAULT NULL,
  #IsExtIdentifier tinyint(4) DEFAULT NULL,

    tooltips = models.CharField(max_length=250, null=True, unique=False, default='') 
    format = models.CharField(max_length=250, null=True, unique=False, default='')

    entity = models.ForeignKey(Entity, related_name="entity_column", blank=True, null=True, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, related_name="rule_column", blank=True, null=True, on_delete=models.CASCADE)
    dataType = models.ForeignKey(DataType, related_name="datatype_column", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns' 
        ordering = ['entity','order']

    def __str__(self):
        return '%s: %s- %s (%s) - %s' % (self.entity, str(self.order), self.columnName, self.dataType, self.columnNameCsd)
  
class Relation(models.Model):
    options = (('primarykey', 'PrimaryKey'), ('foreignkey', 'ForeignKey'), ('none', 'None'))
    optionsJoin = (('inner join', 'inner join'), ('left join', 'left join'), ('right join', 'right join'), ('full join', 'full join'), ('none', 'None'))

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    relationName = models.CharField(max_length=255, null=False, unique=True, default='')
    relationType = models.CharField(max_length=25, default='none', choices=options)
    relationJoin = models.CharField(max_length=25, default='none', choices=optionsJoin)
    
    entityParent = models.ForeignKey(Entity, related_name="entity_parent_relation", blank=True, null=True, on_delete=models.CASCADE)
    entitySon = models.ForeignKey(Entity, related_name="entity_son_relation", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations' 

    def __str__(self):
        return '%s: %s- %s' % (self.relationName, self.entityParent, self.entitySon)

class ConditionRelation(models.Model):
    options = (('=', '='), ('>', '>'), ('<', '<'), ('!=', '!='), ('<>', '<>'))

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    order = models.IntegerField(default=0)

    relation = models.ForeignKey(Relation, related_name="relation_parent_conditionrelation", blank=True, null=True, on_delete=models.CASCADE)
    columnParent = models.ForeignKey(Column, related_name="column_parent_conditionrelation", blank=True, null=True, on_delete=models.CASCADE)
    operator = models.CharField(max_length=2, default='=', choices=options)

    columnSon = models.ForeignKey(Column, related_name="column_son_conditionrelation", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Condition Relation'
        verbose_name_plural = 'Condition Relations' 

    def __str__(self):
        return '%s: %s : %s : %s' % (self.relation, self.columnParent, self.operator, self.columnSon)


 




