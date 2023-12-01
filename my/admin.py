from django.contrib import admin
from my.models import info ,addservice,addproject ,addvideos , myrevies ,blog
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
    
admin.site.register(info,infoAdmin) 


class addserviceAdmin(admin.ModelAdmin):
    list_display=('service_title','service_description')
    
admin.site.register(addservice,addserviceAdmin)    


class addprojectAdmin(admin.ModelAdmin):
    list_display=('portfolioimg','p_title','p_name','p_url','p_catagry')
    
admin.site.register(addproject,addprojectAdmin)  


class addvideosAdmin(admin.ModelAdmin):
    list_display=('videos','v_title','v_description')
    
admin.site.register(addvideos,addvideosAdmin)  


class  myreviewsAdmin(admin.ModelAdmin):
    list_display=('u_imgs','u_name','u_feedback','u_number','u_suggesion',
                  'u_profession','u_rating')
    
admin.site.register(myrevies,myreviewsAdmin)  

class  blogAdmin(admin.ModelAdmin):
    list_display=('B_img','B_catagry','B_subheading','B_description')
    
admin.site.register(blog,blogAdmin)  


