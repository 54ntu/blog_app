from django.contrib import admin
from .models import blogModel,commentModel,messageQuery

# Register your models here.
class blogAdminModel(admin.ModelAdmin):
    list_display=('title','sub_title','desc')


class commentAdminModel(admin.ModelAdmin):
    list_display=('comment','title')


class messageAdminModel(admin.ModelAdmin):
    list_display = ('firstName','lastName','email','message')


admin.site.register(blogModel,blogAdminModel)
admin.site.register(commentModel,commentAdminModel)
admin.site.register(messageQuery,messageAdminModel)