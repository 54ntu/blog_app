from django.contrib import admin
from .models import blogModel

# Register your models here.
class blogAdminModel(admin.ModelAdmin):
    list_display=('title','sub_title','desc')

admin.site.register(blogModel,blogAdminModel)
