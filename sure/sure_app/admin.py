from django.contrib import admin
from sure_app.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Goods)
admin.site.register(Like)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Alarm)
