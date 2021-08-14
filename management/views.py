from django.contrib import messages
from management.models import Modify
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *

# Create your views here.

def pharmacy(request):
    m = Modify.objects.all()
    c = cart_item.objects.all()
    return render(request,"pharmacy.html",{'m':m,'c':c})

    
def about(request):
    return render(request,"about.html")
def shop(request):
    return render(request,"shop.html")

def shop_single1(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_01.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.objects.annotate(
            Quantity = sum('c.Quantity'),
            Price = sum('c.Price')
        )
        c.save()
        
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single1.html")


def shop_single2(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_02.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.save()
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single2.html")


def shop_single3(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_03.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.save()
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single3.html")


def shop_single4(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_04.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.save()
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single4.html")


def shop_single5(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_05.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.save()
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single5.html")


def shop_single6(request):
    if request.method == 'POST':
        c = cart_item()
        img = "../static/images/product_06.png"
        prd = request.POST.get('product')
        pr = float(request.POST.get('price'))
        qu = int(request.POST.get('quantity'))
        tot = pr*qu
        c.Img = img
        c.Product = prd
        c.Quantity = qu
        c.Price = pr
        c.Total = tot
        c.save()
        messages.success(request,"Item added to cart successfully")
        return redirect('shop')
    else:
        return render(request,"shop-single6.html")

def cart(request):
    c = cart_item.objects.all()
    tot = 0
    for i in c:
        tot = tot + i.Total
    return render(request,"cart.html",{'c':c,'tot':tot})
    
def delete(request,pk):
        query = cart_item.objects.get(pk=pk)
        query.delete()
        return redirect('cart')

def checkout(request):
    if request.method=='POST':
        p = pharmacy_order()
        dist = request.POST.get('c_country')
        fname=request.POST.get('c_fname')
        lname=request.POST.get('c_lname')
        add=request.POST.get('c_address')
        pin=request.POST.get('c_postal_zip')
        num=request.POST.get('c_phone')
        ord=request.POST.get('c_order_notes')
        p.District = dist
        p.First_Name=fname
        p.Last_Name=lname
        p.Address=add
        p.pincode=pin
        p.Phone_Number=num
        p.order=ord
        p.save()
        messages.success(request,"Order placed Successfully")
        return redirect('thankyou')
    else:
        c = cart_item.objects.all()
        tot = 0
        for i in c:
            tot = tot + i.Total
        messages.warning(request,"Order not placed")
        return render(request,"checkout.html",{'c':c,'tot':tot})

def index(request):
    if request.method=='POST':
        ap = appointment()
        name=request.POST.get('apname')
        num=request.POST.get('apnum')
        prob=request.POST.get('approb')
        t = request.POST.get('time')
        ap.name=name
        ap.Phone_Number=num
        ap.problem=prob
        ap.appointment_Date = t
        ap.save()
        messages.success(request,"Appointment Sent Successfully")
        return redirect('/')
    else:
        m = Modify.objects.all()
        return render(request,"index2.html",{'m':m})


# def pharm_order(request):
#     if request.method=='POST':
#         p = pharmacy_order()
#         dist = request.POST.get('c_country[]')
#         fname=request.POST.get('c_fname')
#         lname=request.POST.get('c_lname')
#         add=request.POST.get('c_address')
#         pin=request.POST.get('c_postal_zip')
#         num=request.POST.get('c_phone')
#         ord=request.POST.get('c_order_notes')
#         p.District = dist
#         p.First_Name=fname
#         p.Last_Name=lname
#         p.Address=add
#         p.pincode=pin
#         p.Phone_Number=num
#         p.order=ord
#         p.save()
#         messages.success(request,"Order placed Successfully")
#         return redirect('thankyou')
#     else:
#         print('no')
#         # messages.warning(request,"Order not placed")
#         return redirect('pharmacy')

def thankyou(request):
    return render(request,'thankyou.html')