from django.db import models

# Create your models here.
class blogModel(models.Model):
    title=models.CharField(max_length=255)
    sub_title=models.CharField(max_length=255)
    desc=models.TextField(null=False,blank=False)
    blog_img=models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.title}-{self.sub_title}-{self.desc}"