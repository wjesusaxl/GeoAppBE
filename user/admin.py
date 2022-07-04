from django.contrib import admin
from .models import User, Company
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
                    'company'
                    # 'password',
                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Company)