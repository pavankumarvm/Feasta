from django.contrib import admin

from .models import FeastaUser, MessOwner, Consumer
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class FeastaUserAdmin(UserAdmin):

    ordering = ('username',)
    list_display = ('username', 'email', 'is_staff', 'is_consumer', 'is_messowner',)
    search_fields = ('username', 'email',)
    readonly_fields = ('date_joined', 'last_login',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None,{'fields': ('username', 'password')}),
        ('Personal Information',{'fields' : ('first_name', 'last_name', 'email', 'phone_no',)}),
        ('Permissions',{'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('User Type', {'fields': ('is_messowner', 'is_consumer')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login')}),
    )

admin.site.register(FeastaUser, FeastaUserAdmin)
admin.site.register(MessOwner)
admin.site.register(Consumer)