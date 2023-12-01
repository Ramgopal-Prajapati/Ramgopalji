from django.db import models

# Create your models here.
# In info madel save data on user , who send message to me 
class info(models.Model):
      name=models.CharField(max_length=100)
      email=models.CharField(max_length=100)
      subject=models.CharField(max_length=100)
      message=models.CharField(max_length=100)
       
 # In addservice modal add new service which is provided by me       
class addservice(models.Model):
    service_title=models.CharField(max_length=20)
    service_description=models.CharField(max_length=100)
       
class addproject(models.Model):
      portfolioimg=models.FileField(upload_to="static/projectimg")
      p_title=models.CharField(max_length=15)
      p_name=models.CharField(max_length=20)
      p_url=models.SlugField("static/projecturls")      
      p_catagry=models.CharField(max_length=20)
      
      
      
class addvideos(models.Model):
      videos=models.FileField(upload_to="static/myvideos")
      v_title=models.CharField(max_length=15)
      v_description=models.CharField(max_length=100)
      
      
class myrevies(models.Model):
      u_imgs=models.FileField(upload_to="static/userimg")
      u_name=models.CharField(max_length=30)      
      u_profession=models.CharField(max_length=100)
      u_number=models.IntegerField(max_length=10)  
      u_rating=models.CharField(max_length=100)  
      u_feedback=models.CharField(max_length=100)     
      u_suggesion=models.CharField(max_length=100)      
       
       
class blog(models.Model):
      B_img=models.FileField(upload_to="static/blogimg")
      B_catagry=models.TextField(max_length=50 , blank=False , null=False)
      B_description=models.TextField(max_length=150 , blank=False , null=False)
      B_subheading=models.TextField(max_length=50 , blank=False , null=False)
      
           