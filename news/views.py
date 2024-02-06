from django.shortcuts import render,get_object_or_404,redirect
from .models import News
from django.db.models import Q
from .forms import AddNews,AddCategory,Edit
# Create your views here.

def home(request):
    latest_new=News.publish.order_by('-id').first()
    news=News.publish.order_by('-id')[:5]
    sport_news=News.publish.filter(category__name="Sport")
    texno_news=News.publish.filter(category__name="Texnologiya")
    jamiyat_news=News.publish.filter(category__name="jamiyat")
    xorij_news=News.publish.filter(category__name="Xorij")
    context={
        "latest_new":latest_new,
        "news":news,
        "sport_news":sport_news,
        "texno_news":texno_news,
        "jamiyat_news":jamiyat_news,
        "xorij_news":xorij_news,
    }
    return render(request,'index.html',context)



def aloqa(request):
    return render(request,'contact.html')



def single(request,slug):
    news=get_object_or_404(News,slug=slug)
    context={
        "news":news
    }
    return render(request,'single-page.html',context)


def sport_new(request):
    sport_news=News.publish.filter(category__name="Sport")
    context={
        "sport_news":sport_news
    }
    return render(request,'sport_news.html',context)



def texno(request):
    texno=News.publish.filter(category__name="Texnologiya")
    context={
        "texno":texno
    }
    return render(request,'texno.html',context)




def mahaliy_new(request):
    mahaliy=News.publish.filter(category__name="jamiyat")
    context={
        "mahaliy":mahaliy
    }
    return render(request,'jamiyat.html',context)



def xorij(request):
    xo=News.publish.filter(category__name="Xorij")
    context={
        "xo":xo
    }
    return render(request,'xorij.html',context)



def SearchNew(request):
    query=request.GET.get('q')
    results=[]
    if query:
        results=News.object.filter(Q(title__icontains=query)|Q(body__icontains=query),status=News.Status.Published).order_by('publish_time')
    context={
        'results':results,
        'query':query
    }

    return render(request,"search.html",context)



"""Yangilik qo'shish"""
def addnew(request):
    forms=AddNews()
    if request.method=='POST':
        forms=AddNews(request.POST,files=request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('saxifa ')
    context={
            "forms":forms

        }
    return render(request,"add_new.html",context)





"""Category qo'shish"""
def addcat(request):
    forms=AddCategory()
    if request.method=='POST':
        forms=AddCategory(request.POST,files=request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('saxifa')
    context={
            "forms":forms

        }
    return render(request,"add_cat.html",context)








"""Yangiliklni tahrirlash"""
def Editnew(request,slug):
    new=get_object_or_404(News,slug=slug)
    if request.method=='POST':
        forms=Edit(request.POST,instance=new)
        if forms.is_valid():
            forms.save()
            return redirect('saxifa')
    else:
        forms=Edit(instance=new)

    context={
        "forms":forms
    }
    return render(request,"edit_new.html",context)



"""Yangiliklni o'chirish"""
def Delet(request,slug):
    new=get_object_or_404(News,slug=slug)
    if request.method=='POST':
        new.delete()
        return redirect("saxifa")
    context={
        "new":new
    }
    return render(request,"delet.html",context)











