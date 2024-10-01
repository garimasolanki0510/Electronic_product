from django.shortcuts import render
from app1.models import Product_Image
from app_div.models import Product_description
from app_t.models import Product_table

def home(request):
    app1 = Product_Image.objects.all()
    app_div = Product_description.objects.all()
    app_t = Product_table.objects.all()


    if request.method=='GET':
        st=request.GET.get('title')
        if st !=None:
            app_div = Product_description.objects.filter(name__icontains=st)


    rec = {'data1':app1 ,'data2':app_div ,'data3':app_t}
    return render (request ,'index.html',rec)