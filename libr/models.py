from django.db import models
import uuid

# Create your models here.
class AlterationCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    rbg = models.CharField(max_length=30, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class AlterationStyle(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class ColourCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class ColourTone(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class DHSurveyMethod(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    priority = models.IntegerField(default=0)
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Datum(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class GeotHardness(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.Description)

class GeotMatrixType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class GeotShape(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class GeotStrength(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class HoleStatus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class HoleType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Intensity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Labor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class LithologyCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class LithologyGrainSize(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class LithologyTexture(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class LithologyUnit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class MineralCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class MineralStyle(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class MineralZone(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    rbg = models.CharField(max_length=30, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class MineralFill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Oxidation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class QCCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    qcStage = models.CharField(max_length=50, null=False, unique=False, default='')
    qcStageNo = models.IntegerField(default=0)
    parentQCCategoryID = models.IntegerField(default=0)
    orderNo = models.IntegerField(default=0)
    position = models.CharField(max_length=1, null=False, unique=False, default='')
    ratio = models.CharField(max_length=10, null=False, unique=False, default='')
    bgColour = models.CharField(max_length=50, null=False, unique=False, default='')
    fullDescription = models.CharField(max_length=250, null=False, unique=False, default='')
    gridColumn = models.IntegerField(default=0)
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class RockMode(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SGMethod(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SampleCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    priority = models.IntegerField(default=0)
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SampleCondition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SampleMethod(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SampleType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Stratigraphy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructFillTexture(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructFillType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructShape(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructFillThickness(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructName(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructRoughness(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class StructWallRockCompetency(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class Trench(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class WorkArea(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)

class SpecGravMethod(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    code = models.CharField(max_length=10, null=False, unique=False, default='')
    description = models.CharField(max_length=50, null=False, unique=False, default='')
    isActive = models.BooleanField(default=False)
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.Description)