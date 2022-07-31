from django.utils.translation import gettext as _
from django.utils import timezone
from django.db import models
from user.models import User
import uuid

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    company = models.CharField(_('Company'),max_length=25, unique=True)
    tradeName = models.CharField(_('Trade name'),max_length=100, unique=True)
    fiscalName = models.CharField(_('Fiscal name'),max_length=50, unique=True)
    nif = models.CharField(_('NIF'),max_length=25, unique=False)
    country = models.CharField(_('Country'),max_length=25, unique=False)
    legalDomicile = models.CharField(_('Legal domicile'),max_length=100, unique=False)
    state = models.CharField(_('State'),max_length=25, unique=False)
    zipCode = models.CharField(_('Zip code'),max_length=25, unique=False)
    phoneNumber1 = models.CharField(_('Phone number 1'),max_length=25, unique=False)
    phoneNumber2 = models.CharField(_('Phone number 2'),max_length=25, unique=False)
    email = models.EmailField(_('Email'),max_length=254, unique=False)
    web = models.URLField(_('Web'),max_length=250, unique=False)
    contact1 = models.CharField(_('Contact 1'),max_length=50, unique=False)
    positionContact1 = models.CharField(_('Position contact 1'),max_length=50, unique=False)
    phoneNumberContact1 = models.CharField(_('Phone number contact 1'),max_length=25, unique=False)
    contact2 = models.CharField(_('Contact 2'),max_length=50, unique=False)
    positionContact2 = models.CharField(_('Position contact 2'),max_length=50, unique=False)
    phoneNumberContact2 = models.CharField(_('Phone number contact 2'),max_length=25, unique=False)
    logoGeoApp = models.ImageField(upload_to='logo', default='') 
    isActive = models.BooleanField(_('Is Active'),default=False)

     # Log
    createdDateTime = models.DateTimeField(_('Created Date Time'), auto_now_add=True, null=True)
    modifiedDateTime = models.DateTimeField(_('Modified Date Time'), auto_now=True, null=True)
    createdByUserID = models.ForeignKey(User, related_name='companyCustomUserCreate', on_delete=models.DO_NOTHING, default='')
    modifiedByUserID = models.ForeignKey(User, related_name='companyCustomUserModify', on_delete=models.DO_NOTHING, default='')

   
    def __str__(self):
        return self.company

class StatusProject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    shortStatusProject = models.CharField(max_length=2, unique=True)
    isActive = models.BooleanField(_('Is Active'),default=False)
    statusProject = models.CharField(max_length=50, unique=False) #Ingeniería de perfil, Estudio de prefactibilidad (ingeniería conceptual), Estudio de factibilidad (ingeniería básica), Ingeniería de detalle, Ejecución (inversional), Operación
    REQUIRED_FIELDS = ['shortStatusProject','isActive','statusProject']

     # Log
    createdDateTime = models.DateTimeField(_('Created Date Time'), auto_now_add=True, null=True)
    modifiedDateTime = models.DateTimeField(_('Modified Date Time'), auto_now=True, null=True)
    createdByUserID = models.ForeignKey(User, related_name='statusprojectCustomUserCreate', on_delete=models.DO_NOTHING, default='')
    modifiedByUserID = models.ForeignKey(User, related_name='statusprojectCustomUserModify', on_delete=models.DO_NOTHING, default='')
 
    def __str__(self):
        return '%s: %s' % (self.shortStatusProject, self.statusProject)

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    project = models.CharField(_('Project'),max_length=50, unique=True) 
    description = models.CharField(_('Description'),max_length=250, unique=True) 
    isActive = models.BooleanField(_('Is Active'),default=False)
    sortOrder = models.CharField(_('Sort order'),max_length=6, unique=True)
    projectCode = models.CharField(_('Project code'), max_length=5, unique=True, default='?????') 
    photo = models.ImageField(upload_to='photo', unique=False, default='') 

    company  = models.ForeignKey(Company, related_name='projectCompanys', on_delete=models.CASCADE)
    statusProject = models.ForeignKey(StatusProject, related_name='projectStatuss', on_delete=models.CASCADE)
    
    # Log
    createdDateTime = models.DateTimeField(_('Created Date Time'), auto_now_add=True, null=True)
    modifiedDateTime = models.DateTimeField(_('Modified Date Time'), auto_now=True, null=True)
    createdByUserID = models.ForeignKey(User, related_name='projectCustomUserCreate', on_delete=models.DO_NOTHING, default='')
    modifiedByUserID = models.ForeignKey(User, related_name='projectCustomUserModify', on_delete=models.DO_NOTHING, default='')
 
    def __str__(self):
        return '%s: %s' % (self.projectCode, self.project)     

class Role(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    shortUserRol = models.CharField(_('Short use rol'),max_length=3, unique=True)
    isActive = models.BooleanField(_('Active'),default=False)
    role = models.CharField(_('Role'),max_length=25, unique=True) #Ingeniería de perfil, Estudio de prefactibilidad (ingeniería conceptual), Estudio de factibilidad (ingeniería básica), Ingeniería de detalle, Ejecución (inversional), Operación

    REQUIRED_FIELDS = ['shorttatusProject','isActive','statusProject']

    # Log
    createdDateTime = models.DateTimeField(_('Created Date Time'), auto_now_add=True, null=True)
    modifiedDateTime = models.DateTimeField(_('Modified Date Time'), auto_now=True, null=True)
    createdByUserID = models.ForeignKey(User, related_name='roleCustomUserCreate', on_delete=models.DO_NOTHING, default='')
    modifiedByUserID = models.ForeignKey(User, related_name='roleCustomUserModify', on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return '%s: %s' % (self.shortUserRol, self.role)

class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    company  = models.ForeignKey(Company, related_name='teamCompanys', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='teamProjects', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='teamCustomUser', on_delete=models.CASCADE)
    role  = models.ForeignKey(Role, related_name='roleCustomUser', on_delete=models.CASCADE)

    # Log
    createdDateTime = models.DateTimeField(_('Created Date Time'), auto_now_add=True, null=True)
    modifiedDateTime = models.DateTimeField(_('Modified Date Time'), auto_now=True, null=True)
    createdByUserID = models.ForeignKey(User, related_name='teamCustomUserCreate', on_delete=models.DO_NOTHING, default='')
    modifiedByUserID = models.ForeignKey(User, related_name='teamCustomUserModify', on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return '%s: %s' % (self.company, self.project)

