from django.contrib import admin
from .models import User, Company
from view.models import View, EntityView, ColumnView, Dictionary, Filter
from metadata.models import DataType,Entity,Rule,Column,Relation,ConditionRelation,Constraint,EntityType
from functional.models import Company, StatusProject, Project, Role, Team
from config.models import Config
from libr.models import AlterationCode, AlterationStyle, ColourCode, ColourTone, DHSurveyMethod, Datum, GeotHardness, GeotMatrixType, GeotShape, GeotStrength, HoleStatus, HoleType, Intensity, Labor, LithologyCode, LithologyGrainSize, LithologyTexture, LithologyUnit, MineralCode, MineralStyle, MineralZone, MineralFill, Oxidation, QCCategory, RockMode, SGMethod, SampleCategory, SampleCondition, SampleMethod, SampleType, Stratigraphy, StructFillTexture, StructFillType, StructName, StructShape, StructRoughness, StructFillThickness, StructType, StructWallRockCompetency, Trench, WorkArea, SpecGravMethod
from drillhole.models import Collar, Survey, GeoTechDetail, Lithology, GeoTech, Alteration, Sample, SpecificGravity, Mineral, SampleQC
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'email',
                    'username',
                    # 'uuid',
                    # 'date_joined',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                    # 'company'
                    # 'password',
                    'external_id'
                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Entity)
admin.site.register(DataType)
admin.site.register(Column)
admin.site.register(Rule)
admin.site.register(Relation)
admin.site.register(ConditionRelation)
admin.site.register(Constraint)
admin.site.register(EntityType)


admin.site.register(Company)
admin.site.register(StatusProject)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Team)

admin.site.register(Config)

admin.site.register(View)
admin.site.register(Dictionary)
admin.site.register(EntityView)
admin.site.register(ColumnView)
admin.site.register(Filter)

admin.site.register(AlterationCode) 
admin.site.register(AlterationStyle) 
admin.site.register(ColourCode) 
admin.site.register(ColourTone) 
admin.site.register(DHSurveyMethod) 
admin.site.register(Datum) 

admin.site.register(GeotHardness) 
admin.site.register(GeotMatrixType) 
admin.site.register(GeotShape) 
admin.site.register(GeotStrength) 

admin.site.register(HoleStatus) 
admin.site.register(HoleType) 

admin.site.register(Intensity) 
admin.site.register(Labor) 

admin.site.register(LithologyCode) 
admin.site.register(LithologyGrainSize) 
admin.site.register(LithologyTexture) 
admin.site.register(LithologyUnit) 

admin.site.register(MineralCode) 
admin.site.register(MineralStyle) 
admin.site.register(MineralZone) 
admin.site.register(MineralFill)

admin.site.register(Oxidation) 
admin.site.register(QCCategory) 
admin.site.register(RockMode) 

admin.site.register(SGMethod) 

admin.site.register(SampleCategory) 
admin.site.register(SampleCondition) 
admin.site.register(SampleMethod) 
admin.site.register(SampleType)

admin.site.register(Stratigraphy) 

admin.site.register(StructFillTexture) 
admin.site.register(StructFillType) 
admin.site.register(StructName) 
admin.site.register(StructShape)
admin.site.register(StructFillThickness)
admin.site.register(StructRoughness) 
admin.site.register(StructType) 
admin.site.register(StructWallRockCompetency) 
admin.site.register(Trench) 
admin.site.register(WorkArea)
admin.site.register(SpecGravMethod)

admin.site.register(Collar)
admin.site.register(Survey) 
admin.site.register(GeoTechDetail)
admin.site.register(Lithology)
admin.site.register(GeoTech)
admin.site.register(Alteration)
admin.site.register(Sample)
admin.site.register(SpecificGravity)
admin.site.register(Mineral)
admin.site.register(SampleQC)