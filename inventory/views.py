from django.shortcuts import render
from .models import Product
# from django.db.models import Q
from datetime import date,time
def home(request):
    products = Product.objects.all()  
    # products = Product.objects.filter(name__exact='Butter')  
    # products = Product.objects.filter(name__iexact='butter')  
    # products = Product.objects.filter(category__contains='er')  
    # products = Product.objects.filter(category__icontains='er')  
    # products = Product.objects.filter(id__in=[1,5,7])  
    # products = Product.objects.filter(stock__in=[40])  
    # products = Product.objects.filter(stock__gt=70)  
    # products = Product.objects.filter(stock__gte=40)  
    # products = Product.objects.filter(stock__lt=100)  
    # products = Product.objects.filter(stock__lte=40)  
    # products = Product.objects.filter(name__startswith='S')  
    # products = Product.objects.filter(name__istartswith='m')  
    # products = Product.objects.filter(name__endswith='O')  
    # products = Product.objects.filter(name__endswith='o')  
    # products = Product.objects.filter(price__range=(50, 200))
    # products = Product.objects.filter(added_on__date__range=(date(2024, 1, 1), date(2025, 6, 1)))
    # products = Product.objects.filter(added_on__date=date(2025, 6, 19))
    # products = Product.objects.filter(added_on__year=2025)
    # products = Product.objects.filter(added_on__year__gt=2024)
    # products = Product.objects.filter(added_on__month=6)
    # products = Product.objects.filter(added_on__week=25)
    # products = Product.objects.filter(added_on__week_day=4)  # Wednesday
    # products = Product.objects.filter(added_on__quarter=2)
    # products = Product.objects.filter(added_on__time__gt=time(12, 0))
    # products = Product.objects.filter(added_on__hour=10)
    # products = Product.objects.filter(added_on__minute__gt=30)
    # products = Product.objects.filter(added_on__second__lte=30)
    # products = Product.objects.filter(description__isnull=False)
    # products = Product.objects.filter(name__regex=r'^B.*')        # Starts with 'B'
    # products = Product.objects.filter(name__iregex=r'butter|milk')
       
    print('return:',products)
    print()
    print(products.query)
    return render(request, 'inventory/product_list.html', {'products': products})
