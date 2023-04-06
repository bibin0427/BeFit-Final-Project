from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.http import HttpResponse
from Adminside.models import admindb,catdb,prodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def indexfile(req):
    return render(req,"index.html")

def adminpage(req):
    return render(req,"Addadmin.html")
def admindata(request):
    if request.method == "POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        mo=request.POST.get('mob')
        us=request.POST.get('username')
        ps=request.POST.get('password')
        img=request.FILES['image']

        obj=admindb(Name=na,Email=em,Mobile=mo,Username=us,Password=ps,Image=img)
        obj.save()
        return redirect(adminpage)

def displayadmin(request):
    data=admindb.objects.all()
    return render(request,"Display Admin.html", {'data':data})
def editcustm(req,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(req,"Edit Admin.html",{'data':data})

def updatedata(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mo = request.POST.get('mob')
        us = request.POST.get('username')
        ps = request.POST.get('password')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update( Name=na,Email=em,Mobile=mo,Username=us,Password=ps,Image=file)

        return redirect(displayadmin)

def deletedata(req,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)

# Category
def catpage(req):
    return render(req,"Add Category.html")
def catdata(req):
    if req.method == "POST":
        na=req.POST.get('name')
        ds=req.POST.get('description')
        img=req.FILES['image']

        obj=catdb(Name=na,Description=ds,Image=img)
        obj.save()
        return redirect(catpage)

#display category
def displaycat(request):
    data=catdb.objects.all()
    return render(request,"Display Category .html", {'data':data})
def editcat(req,dataid):
    data=catdb.objects.get(id=dataid)
    return render(req,"Edit Category.html",{'data':data})

def updatecatdata(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')

        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update( Name=na,Description=ds,Image=file)

        return redirect(displaycat)

def deletecatdata(req,dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycat)

#
# # Product

def productpage(req):
    return render(req,"Add Product.html")

def productdata(req):

    if req.method == "POST":
        cat=req.POST.get('category')
        na=req.POST.get('name')
        pr=req.POST.get('price')
        qty=req.POST.get('quantity')
        des=req.POST.get('description')
        img=req.FILES['image']

        obj=prodb(Name=na,Price=pr,Quantity=qty,Description=des,Image=img,Category=cat)
        obj.save()
        return redirect(productpage)
#
#     # display product
#
def displayproduct(request):
    data=prodb.objects.all()
    return render(request,"Display Product.html", {'data':data})
def editproduct(req,dataid):
    data=prodb.objects.get(id=dataid)
    print(data)
    return render(req,"Edit Product.html",{'data':data})

def updateproduct(request,dataid):
    if request.method == "POST":
        cat = request.POST.get('category')
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qty = request.POST.get('quantity')
        ds = request.POST.get('description')


        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=dataid).Image
        prodb.objects.filter(id=dataid).update( Category=cat,Name=na,Price=pr,Quantity=qty,Description=ds,Image=file)

        return redirect(displayproduct)

def deleteprodata(req,dataid):
    data=prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
#
# #loginpage
def loginpage(req):
    return render(req,"Login .html")
# def myfunction(request):
#     return HttpResponse("<h1>Login<h2>")
#
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user= authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexfile)
            else:
                return redirect(loginpage)

        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

#contactpage