from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.Exemple_api import start
from api.ClothMeasure_masc import run
import urllib

from .models import * 
from .forms import *
from .forms import CreateUserForm


def index(request): 
    return render(request, 'index.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('user_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Conta criada com Sucesso ' + user)
                return redirect('login')
        
        context = {'form':form}
        return render(request, 'register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_page')
    else:  
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_page')
            else:
                messages.info(request, 'Nome ou senha incorretos')

        return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('index')

def about(request):

    about1 = About.objects.create(
        description ="",
        img = "static/images/chose1.png",
    )

    about2 = About.objects.create(
        description ="",
        img = "static/images/chose1.png",
    )
    
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):

    feature1 = Features.objects.create(
        name="Algoritmo de Extração de Medidas corporais",
        description="Ao você enviar uma foto de corpo todo, preferencialmente atrás de um fundo branco e com braços abertos. Logo após isso informar a sua altura, o algoritmo irá extrair as medidas do seu corpo e mostrar os resultados.",
        img_logo="static/images/chose1.png",
        url="bodyMeasure."
    )

    feature2 = Features.objects.create(
        name="Vestimento Ideal",
        description="Tamanho de roupa ideal",
        img_logo="static/images/chose1.png",
        url="clothMeasure."
    )

    features = Features.objects.all()

    return render(request, 'services.html', {'features': features})

def _grab_image(path=None, stream=None, url=None):
    if path is not None:
        return path
    else:
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()
        elif stream is not None:
            data = stream.read()

        temp_file = 'temp_image.jpg'
        with open(temp_file, 'wb') as f:
            f.write(data)
        return temp_file

@login_required(login_url='login')
def user_page(request):
    return render(request, 'user_page.html')

@login_required(login_url='login')
def bodyMeasure(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if request.FILES.GET("image", None) is not None:
            img_path = _grab_image(stream=request.FILES["image"])
            height_cm = int(request.POST.get('height_cm'))
            
            image_results = start(img_path, height_cm)

            #Resultados ilustrativos
            forearm = 40
            arm = 60
            waist_shoulder = 50
            leg = 80
            bust = 40
            waist_knee = 60

            cloth_measure = run(forearm, arm, waist_shoulder, leg, bust, waist_knee)
            tam_camiseta = (cloth_measure['camiseta'])
            tam_camisa = (cloth_measure['camisa'])
            tam_calca = (cloth_measure['calca'])
            tam_bermuda = (cloth_measure['bermuda'])

            return render(request, 'bodyMeasure.html', {'form': form, 'image_results': image_results, 'image': img_path, 'tam_camiseta': tam_camiseta,'height_cm': height_cm, 'tam_camisa': tam_camisa, 'tam_calca': tam_calca, 'tam_bermuda': tam_bermuda})
    else:
        form = ImageForm()
    return render(request, 'bodyMeasure.html', {'form': form})


@login_required(login_url='login')
def clothMeasure(request):
    return render(request, 'clothMeasure.html')

@login_required(login_url='login')
def measureDate(request):
    return render(request, 'measureDate.html')

@login_required(login_url='login')
def user_services(request):
    return render(request, 'user_services.html')

# @login_required(login_url='login;)
# def servicos_disponiveis(request):
#     medidas = MedidaCorporal.objects.filter(usuario=request.user)
#     return render(request, 'servicos_disponiveis.html', {'medidas': medidas})

# urlpatterns = [
#     path('servicos/', views.servicos_disponiveis, name='servicos_disponiveis'),
# ]