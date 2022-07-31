import uuid
from django.db import models
from functional.models import Company, Project  
from lib.models import *  
from user.models import User  

class Collar(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    holeId = models.CharField(max_length=20, null=False, unique=False, default='')
    MaxDepth = models.FloatField()
    gridId = models.IntegerField(default=0)
    East = models.FloatField(null=False)
    North = models.FloatField(null=False)
    rl = models.FloatField()
    surveyDate = models.DateTimeField()
    area = models.CharField(max_length=50, null=False, unique=False, default='')
    dateStarted = models.DateTimeField()
    dateCompleted = models.DateTimeField()
    validated = models.IntegerField(default=0)
    validatedDate = models.DateTimeField()
 
    company  = models.ForeignKey(Company, related_name='collarCompanys', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='collarProjects', on_delete=models.CASCADE)
    holeType = models.ForeignKey(HoleType, related_name='collarHoleTypes', on_delete=models.CASCADE)
    holeStatusID = models.ForeignKey(HoleStatus, related_name='collarHoleStatus', on_delete=models.CASCADE)
    dhSurveyMethod = models.ForeignKey(DHSurveyMethod, related_name='collarDhsurveymethods', on_delete=models.CASCADE)
    surveByUser = models.ForeignKey(User, related_name='collarSurveUser', on_delete=models.CASCADE)
    geologistUser = models.ForeignKey(User, related_name='collarGeologistUsers', on_delete=models.CASCADE)
    contractortUser = models.ForeignKey(User, related_name='collarContactorUsers', on_delete=models.CASCADE)
    validatedByUser = models.ForeignKey(User, related_name='collarValidatedByUsers', on_delete=models.CASCADE)
    responsibleUser = models.ForeignKey(User, related_name='collarResponsibleUsers', on_delete=models.CASCADE)

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='collarUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.holeId

class Survey(models.Model):  
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='surveyCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    dip = models.FloatField()
    azimuth = models.FloatField()

    dhSurveyMethod = models.ForeignKey(DHSurveyMethod, related_name='surveyDhsurveymethods', on_delete=models.CASCADE)

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='surveyUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class GeoTechDetail(models.Model):  
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='geotechdetailCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    length = models.FloatField()

    structureAngle = models.CharField(max_length=5, null=False, unique=False, default='')
    structureCount = models.IntegerField(default=0)
    displacementDirection = models.CharField(max_length=10, null=False, unique=False, default='')
    displacementAmountMM = models.FloatField()
    rmr = models.FloatField()

    structType = models.ForeignKey(StructType, related_name='geotechdetailStructTypes', on_delete=models.CASCADE)
    intensity = models.ForeignKey(Intensity, related_name='geotechdetailIntensitys', on_delete=models.CASCADE)
    structWallRockCompetency = models.ForeignKey(StructWallRockCompetency, related_name='geotechdetailStructWallRockCompetencys', on_delete=models.CASCADE)  
    structRoughness = models.ForeignKey(StructRoughness, related_name='geotechdetailStructRoughness', on_delete=models.CASCADE)
    structFillType = models.ForeignKey(StructFillType, related_name='geotechdetailStructFillTypes', on_delete=models.CASCADE)
    structFillTexture = models.ForeignKey(StructFillTexture, related_name='geotechdetailStructFillTextures', on_delete=models.CASCADE)
    structFillThickness = models.ForeignKey(StructFillThickness, related_name='geotechdetailStructFillThickness', default='', on_delete=models.CASCADE)
    mineralFill1 = models.ForeignKey(MineralFill, related_name='geotechdetailMineralFill1', default='', on_delete=models.CASCADE)
    mineralFill2 = models.ForeignKey(MineralFill, related_name='geotechdetailMineralFill2', default='', on_delete=models.CASCADE)

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='geotechdetailUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class Lithology(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='lithologyCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    lith1PC = models.FloatField()
    lith2PC = models.FloatField()

    lithologyCode1 = models.ForeignKey(LithologyCode, related_name='lithologyLithologyCodes1', on_delete=models.CASCADE), 
    lithologyTexture1 = models.ForeignKey(LithologyTexture, related_name='lithologyLithologyTextures1', on_delete=models.CASCADE)
    structName1 = models.ForeignKey(StructName, related_name='lithologyStructNames1', on_delete=models.CASCADE) 
    lithologyGrainSize1 = models.ForeignKey(LithologyGrainSize, related_name='lithologyLithologyGrainSizes1', on_delete=models.CASCADE) 
    lithologyUnit1 = models.ForeignKey(LithologyUnit, related_name='lithologyLithologyUnits1', on_delete=models.CASCADE) 
    oxidation1 = models.ForeignKey(Oxidation, related_name='lithologyOxidations1', on_delete=models.CASCADE) 
    colourTone1 = models.ForeignKey(ColourTone, related_name='lithologyColourTones1', on_delete=models.CASCADE) 
    colourCode1A = models.ForeignKey(ColourCode, related_name='lithologyColourCodes1A', on_delete=models.CASCADE) 
    colourCode1B = models.ForeignKey(ColourCode, related_name='lithologyColourCodes1B', on_delete=models.CASCADE) 
    stratigraphy1 = models.ForeignKey(Stratigraphy, related_name='lithologyStratigraphys1', on_delete=models.CASCADE) 
    lithologyCode2 = models.ForeignKey(LithologyCode, related_name='lithologyLithologyCodes2', on_delete=models.CASCADE), 
    lithologyTexture2 = models.ForeignKey(LithologyTexture, related_name='lithologyLithologyTextures2', on_delete=models.CASCADE)
    structName2 = models.ForeignKey(StructName, related_name='lithologyStructNames2', on_delete=models.CASCADE) 
    lithologyGrainSize2 = models.ForeignKey(LithologyGrainSize, related_name='lithologyLithologyGrainSizes2', on_delete=models.CASCADE) 
    lithologyUnit2 = models.ForeignKey(LithologyUnit, related_name='lithologyLithologyUnits2', on_delete=models.CASCADE) 
    oxidation2 = models.ForeignKey(Oxidation, related_name='lithologyOxidations2', on_delete=models.CASCADE) 
    colourTone2 = models.ForeignKey(ColourTone, related_name='lithologyColourTones2', on_delete=models.CASCADE) 
    colourCode2A = models.ForeignKey(ColourCode, related_name='lithologyColourCodes2A', on_delete=models.CASCADE) 
    colourCode2B = models.ForeignKey(ColourCode, related_name='lithologyColourCodes2B', on_delete=models.CASCADE) 
    stratigraphy2 = models.ForeignKey(Stratigraphy, related_name='lithologyStratigraphys2', on_delete=models.CASCADE) 
    intensity = models.ForeignKey(Intensity, related_name='lithologyIntensitys2', on_delete=models.CASCADE)  

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='lithologyUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class GeoTech(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='geoTechCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    recoveryM = models.FloatField()
    recoveryPercentage = models.FloatField()
    totalSolidCore = models.FloatField()
    totalMaxtrixCore = models.FloatField(),
    numFractures = models.IntegerField(default=0)
    fracFreqPerM = models.IntegerField(default=0)
    MaterialDescription = models.CharField(max_length=255, null=False, unique=False, default='')

    geotMatrixType = models.ForeignKey(GeotMatrixType, related_name='geoTechGeotMatrixTypes', on_delete=models.CASCADE) 
    geotStrength = models.ForeignKey(GeotStrength, related_name='geoTechGeotStrengths', on_delete=models.CASCADE)  
    geotHardness = models.ForeignKey(GeotHardness, related_name='geoTechGeotHardness', on_delete=models.CASCADE)

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='geoTechUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class Alteration(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='alterationCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    length = models.FloatField()

    alterationCode1 = models.ForeignKey(AlterationCode, related_name='alterationAlterationCodes1', on_delete=models.CASCADE)
    intensity1 = models.ForeignKey(Intensity, related_name='alterationIntensitys1', on_delete=models.CASCADE)
    alterationStyle1 = models.ForeignKey(AlterationStyle, related_name='alterationAlterationStyles1', on_delete=models.CASCADE)   
    alterationCode2 = models.ForeignKey(AlterationCode, related_name='alterationAlterationCodes2', on_delete=models.CASCADE)
    intensity2 = models.ForeignKey(Intensity, related_name='alterationIntensitys2', on_delete=models.CASCADE)
    alterationStyle2 = models.ForeignKey(AlterationStyle, related_name='alterationAlterationStyles2', on_delete=models.CASCADE)   
    alterationCode3 = models.ForeignKey(AlterationCode, related_name='alterationAlterationCodes3', on_delete=models.CASCADE)
    intensity3 = models.ForeignKey(Intensity, related_name='alterationIntensitys3', on_delete=models.CASCADE)
    alterationStyle3 = models.ForeignKey(AlterationStyle, related_name='alterationAlterationStyles3', on_delete=models.CASCADE)   
    alterationCode4 = models.ForeignKey(AlterationCode, related_name='alterationAlterationCodes4', on_delete=models.CASCADE)
    intensity4 = models.ForeignKey(Intensity, related_name='alterationIntensitys4', on_delete=models.CASCADE)
    alterationStyle4 = models.ForeignKey(AlterationStyle, related_name='alterationAlterationStyles4', on_delete=models.CASCADE)   
    alterationCode5 = models.ForeignKey(AlterationCode, related_name='alterationAlterationCodes5', on_delete=models.CASCADE)
    intensity5 = models.ForeignKey(Intensity, related_name='alterationIntensitys5', on_delete=models.CASCADE)
    alterationStyle5 = models.ForeignKey(AlterationStyle, related_name='alterationAlterationStyles5', on_delete=models.CASCADE)   

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='alterationUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class Sample(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='sampleCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    sampleID = models.IntegerField(default=0)
    sampleType = models.ForeignKey(SampleType, related_name='sampleSampleType', default='', on_delete=models.CASCADE) 
    historicalSampleID  = models.CharField(max_length=255, null=False, unique=False, default='')

    gridID = models.IntegerField(default=0)
    sampleRecoveryPCT = models.FloatField()
    sampleWeightKG = models.FloatField()
    contamination = models.CharField(max_length=50, null=False, unique=False, default='')
    isSuperseded = models.BooleanField(default=False)
    hasDuplicate = models.BooleanField(default=False)
    east= models.FloatField(null=False)
    north= models.FloatField(null=False)
    rl = models.FloatField()
    bin = models.CharField(max_length=20, null=False, unique=False, default='')
    pickUpDateTime = models.DateTimeField()

    structType = models.ForeignKey(StructType, related_name='sampleStructTypes', on_delete=models.CASCADE)
    sampleMethod = models.ForeignKey(SampleMethod, related_name='sampleSampleMethods', on_delete=models.CASCADE) 
    sampleCategory = models.ForeignKey(SampleCategory, related_name='sampleSampleCategorys', on_delete=models.CASCADE) 
    sampleCondition = models.ForeignKey(SampleCondition, related_name='sampleSampleConditions', on_delete=models.CASCADE)

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    sampleDateTime = models.DateTimeField()
    sampleByUserID = models.ForeignKey(User, related_name='sampleUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class SampleQC(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='sampleqcCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    sampleID = models.IntegerField(default=0)
    sampleType = models.ForeignKey(SampleType, related_name='sampleqcSampleType', default='', on_delete=models.CASCADE) 
    historicalSampleID  = models.CharField(max_length=255, null=False, unique=False, default='')

    origSample = models.ForeignKey(Sample, related_name='sampleqcOrigSamples', on_delete=models.CASCADE) 
    qcCategory = models.ForeignKey(QCCategory, related_name='sampleqcQCCategory', on_delete=models.CASCADE)  
    sampleMethod = models.ForeignKey(SampleMethod, related_name='sampleqcSampleMethods', on_delete=models.CASCADE) 

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    sampleDateTime = models.DateTimeField()
    sampleByUserID = models.ForeignKey(User, related_name='sampleqcUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class SpecificGravity(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    collar = models.ForeignKey(Collar, related_name='specificgravityCollars', on_delete=models.CASCADE)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    repeatValue = models.IntegerField(default=0)
    weightWetG = models.FloatField()
    weightDryG = models.FloatField()
    reading = models.CharField(max_length=10, null=False, unique=False, default='')
    unitCode = models.CharField(max_length=10, null=False, unique=False, default='')
    comments = models.CharField(max_length=255, null=False, unique=False, default='')

    sample = models.ForeignKey(Sample, related_name='specificgravitySamples', on_delete=models.CASCADE) 
    sampleType = models.ForeignKey(SampleType, related_name='specificgravitySampleType', default='', on_delete=models.CASCADE) 
    specGravMethod = models.ForeignKey(SpecGravMethod, related_name='specificgravitySpecGravMethod', default='', on_delete=models.CASCADE) 

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    sampleDateTime = models.DateTimeField()
    sampleByUserID = models.ForeignKey(User, related_name='specificgravityUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

class Mineral(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    depthFrom = models.FloatField()
    depthTo = models.FloatField()

    mineralCode1 = models.ForeignKey(MineralCode, related_name='mineralMineralCodes1', on_delete=models.CASCADE)  
    mineralPercentage1 = models.FloatField()
    mineralStyle1 = models.ForeignKey(MineralStyle, related_name='mineralMineralStyles1', on_delete=models.CASCADE)  
    mineralCode2 = models.ForeignKey(MineralCode, related_name='mineralMineralCodes2', on_delete=models.CASCADE)  
    mineralPercentage2 = models.FloatField()
    mineralStyle2 = models.ForeignKey(MineralStyle, related_name='mineralMineralStyles2', on_delete=models.CASCADE)  
    mineralCode3 = models.ForeignKey(MineralCode, related_name='mineralMineralCodes3', on_delete=models.CASCADE)  
    mineralPercentage3 = models.FloatField()
    mineralStyle3 = models.ForeignKey(MineralStyle, related_name='mineralMineralStyles3', on_delete=models.CASCADE)  
    mineralCode4 = models.ForeignKey(MineralCode, related_name='mineralMineralCodes4', on_delete=models.CASCADE)  
    mineralPercentage4 = models.FloatField()
    mineralStyle4 = models.ForeignKey(MineralStyle, related_name='mineralMineralStyles4', on_delete=models.CASCADE)  
    mineralCode5 = models.ForeignKey(MineralCode, related_name='mineralMineralCodes5', on_delete=models.CASCADE)  
    mineralPercentage5 = models.FloatField()
    mineralStyle5 = models.ForeignKey(MineralStyle, related_name='mineralMineralStyles5', on_delete=models.CASCADE)  

    intensity = models.ForeignKey(Intensity, related_name='mineralIntensity', on_delete=models.CASCADE)   

    comments = models.CharField(max_length=255, null=False, unique=False, default='')
    dataSource = models.CharField(max_length=255, null=False, unique=False, default='')
    loggedDateTime = models.DateTimeField()
    loggedByUser = models.ForeignKey(User, related_name='mineralUsers', on_delete=models.CASCADE)

    def __str__(self):
        return self.depthFrom

