from django.db import models

# Create your models here.
class blogModel(models.Model):
    title=models.CharField(max_length=255,null=True)
    sub_title=models.CharField(max_length=255)
    desc=models.TextField(null=False,blank=False)
    blog_img=models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return self.title
    

class commentModel(models.Model):
    comment=models.TextField(null=False,blank=False)
    title=models.ForeignKey(blogModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    