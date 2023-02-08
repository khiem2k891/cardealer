from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'year_search': year_search,
        'body_style': body_style,
    }
    return render(request, 'car/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'car/car_detail.html', data)



