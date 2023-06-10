from django.db import models

# Create your models here.
class blogModel(models.Model):
    title=models.CharField(max_length=255,null=True)
    sub_title=models.CharField(max_length=255)
    desc=models.TextField(null=False,blank=False)
    blog_img=models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return f"{self.title}-{self.sub_title}-{self.desc}"
    

class commentModel(models.Model):
    comment=models.TextField(null=False,blank=False)
    # commented_at=models.DateTimeField(auto_now=True)
    title=models.ForeignKey(blogModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}-{self.commented_at} {self.title}"
    