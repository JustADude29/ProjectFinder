from django.contrib import admin
from Info_Data.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('Name','E_mail','Programme','Department','Year')

admin.site.register ( User , UserAdmin )