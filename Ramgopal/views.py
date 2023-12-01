from django.shortcuts import render , redirect
from my.models import info , addservice , addproject ,addvideos , myrevies , blog
from my.models import myrevies




def Home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        
        re=info(name=name,email=email,subject=subject,message=message)
        re.save()
        
    alldata=addservice.objects.all()
    all1=addvideos.objects.all()
    all2=addproject.objects.all()
    all3=myrevies.objects.all()
    all4=blog.objects.all()
    data={
        'alldata':alldata,
        'all1':all1,
        'all2':all2,
        'all3':all3,
        'all4':all4
    }
    # allproject=addproject.objects.all()
    # data={
    #     'allproject':allproject
    # }
    
    return render(request,"index.html",data)



def Review(request):
    if request.method=="POST":
        u_suggesion=request.POST.get("u_suggesion")
        u_name=request.POST.get("u_name")
        u_number=request.POST.get("u_number")
        u_imgs=request.POST.get("u_imgs")
        u_profession=request.POST.get("u_profession")
        u_rating=request.POST.get("u_rating")
        u_feedback=request.POST.get("u_feedback")
        
        re=myrevies(u_name=u_name,u_suggesion=u_suggesion,u_number=u_number,u_imgs=u_imgs,u_profession=u_profession,u_rating=u_rating,u_feedback=u_feedback)
        re.save()
        
        
        # return redirect(request,"index.html")
    return render(request,"reviews.html")