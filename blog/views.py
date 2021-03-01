from django.shortcuts import render, redirect
from .forms import DogsForm, UserRegisterForm

from .models import Dogs, Deals
from django.views import generic
from django.urls import reverse_lazy


# вывод списка всех офисов
def index(request):
    dogs = Dogs.objects.all()
    context = {
        'dogs': dogs,
        'title': 'Наши Собаки'
    }

    return render(request, template_name='blog/index.html', context=context)


# детализация по айди собаки
def by_dog(request, dog_id):
    current_dog = Dogs.objects.get(pk=dog_id)
    context = {
        'current_dog': current_dog,
        'message': ""
    }

    return render(request, 'blog/by_dog.html', context)


# добавление собаки
def image_upload_view(request):
    if request.method == 'POST':
        form = DogsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DogsForm()
    return render(request, 'blog/createDogs.html', {'form': form})


# регистрация
class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# отображение заявок пользователя
def get_deals(request):
    if request.user.is_staff:
        applications = Deals.objects.all()
    else:
        applications = Deals.objects.all().filter(client=request.user)
    context = {
        'apps': applications
    }

    return render(request, template_name='blog/deals.html', context=context)


# подать заявку на собаку
def add_deal(request, dog_id):
    current_dog = Dogs.objects.get(pk=dog_id)
    try:
        Deals.objects.get(client=request.user, dogs=current_dog)
        context = {
            "message": "Вы уже подавали заявку на данную собаку",
            'current_dog': current_dog
        }
        return render(request, 'blog/by_dog.html', context)
    except Deals.DoesNotExist:
        new_deal = Deals(client=request.user, dogs=current_dog, additionalInfo=request.POST['addInfo'])
        new_deal.save()
        deals = Deals.objects.all().filter(client=request.user)
        context = {
            'deals': deals
        }
        return render(request, 'blog/deals.html', context)
