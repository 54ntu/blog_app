from django.contrib import admin
from .models import blogModel,commentModel

# Register your models here.
class blogAdminModel(admin.ModelAdmin):
    list_display=('title','sub_title','desc')


class commentAdminModel(admin.ModelAdmin):
    list_display=('comment','title')

admin.site.register(blogModel,blogAdminModel)
admin.site.register(commentModel,commentAdminModel)
