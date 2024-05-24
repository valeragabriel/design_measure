from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.Exemple_api import start
from api.ClothMeasure_masc import run
from api.input_clothMeasure import main
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

@login_required(login_url='login')
def user_page(request):
    return render(request, 'user_page.html')

@login_required(login_url='login')
def bodyMeasure(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if request.FILES.get("image", None) is not None:
            img_path = _grab_image(stream=request.FILES["image"])
            height_cm = int(request.POST.get('height_cm'))
            
            image_results = start(img_path, height_cm)

            # Resultados ilustrativos
            # Esses reais resultados são obtidos através do algoritmo de extração de medidas corporais
            # Só estou mostrando como chama uma api e como funciona a lógica de aplica-la 
            cloth_measure = run(forearm=26, arm=53, waist_shoulder=62, leg=85, bust=60, waist_knee=50, waist=105)
            tam_camiseta = (cloth_measure['camiseta'])
            tam_camisa = (cloth_measure['camisa'])
            tam_calca = (cloth_measure['calca'])
            tam_bermuda = (cloth_measure['bermuda'])

            return render(request, 'results.html', {'form': form, 'image_results': image_results, 'image': img_path, 'tam_camiseta': tam_camiseta,'height_cm': height_cm, 'tam_camisa': tam_camisa, 'tam_calca': tam_calca, 'tam_bermuda': tam_bermuda, 'height_cm': height_cm})
    else:
        form = ImageForm()
    return render(request, 'bodyMeasure.html', {'form': form})

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
def clothMeasure(request):
    return render(request, 'clothMeasure.html')

@login_required(login_url='login')
def measureDate(request):
    return render(request, 'measureDate.html')

@login_required(login_url='login')
def user_services(request):

    feature1 = Features.objects.create(
        name="Extração de Medidas corporais",
        description="Informe sua altura, e envie uma foto, para  descobrir suas medidas corporais.",
        img_logo="/images/Measure_reference.png",
        url="bodyMeasure"
    )

    feature2 = Features.objects.create(
        name="Vestimento Ideal",
        description="Através das suas medidas corporais enviadas encontramos o tamanho de roupa ideal para você, com base nas medidas de uma loja padrão.",
        img_logo="/images/measure_cloth1.png",
        url="clothMeasure"
    )

    feature3 = Features.objects.create(
        name="Vestimento Ideal, com base na sua loja de interesse ",
        description="Através das suas medidas corporais enviadas encontramos o tamanho de roupa ideal para você, entretanto você que define o tamanhos de medidas das roupas. ",
        img_logo="/images/measure_cloth2.png",
        url="clothMeasure2"
    )

    features = [feature1, feature2, feature3]
    return render(request, 'user_services.html', {'features': features})

@login_required(login_url='login')
def results(request):
    return render(request, 'results.html')

@login_required(login_url='login')
def clothMeasure2(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if request.FILES.get("image", None) is not None:
            img_path = _grab_image(stream=request.FILES["image"])
            height_cm = int(request.POST.get('height_cm'))

            image_results = start(img_path, height_cm)

            blusa_PP  = int(request.POST.get('blusa_PP'))
            blusa_P  = int(request.POST.get('blusa_P'))
            blusa_M  = int(request.POST.get('blusa_M'))
            blusa_G  = int(request.POST.get('blusa_G'))
            blusa_GG = int(request.POST.get('blusa_GG'))
            busto_PP  = int(request.POST.get('busto_PP'))
            busto_P  = int(request.POST.get('busto_P'))
            busto_M  = int(request.POST.get('busto_M'))
            busto_G  = int(request.POST.get('busto_G'))
            busto_GG = int(request.POST.get('busto_GG'))
            manga_PP  = int(request.POST.get('manga_PP'))
            manga_P  = int(request.POST.get('manga_P'))
            manga_M  = int(request.POST.get('manga_M'))
            manga_G  = int(request.POST.get('manga_G'))
            manga_GG = int(request.POST.get('manga_GG'))
            modelagem = request.POST.get('modelagem')
    
            
            cloth_measure = main(blusa_PP, blusa_P, blusa_M, blusa_G, blusa_GG, busto_PP, busto_P, busto_M, busto_G, busto_GG, manga_PP, manga_P, manga_M, manga_G, manga_GG, modelagem)
            tam_camiseta = (cloth_measure['camiseta'])
            
            return render(request, 'results_clothMeasure2.html', {'form': form, 'image_results': image_results, 'image': img_path, 'tam_camiseta': tam_camiseta,'height_cm': height_cm, 'blusa_PP': blusa_PP, 'blusa_P': blusa_P, 'blusa_M': blusa_M, 'blusa_G': blusa_G, 'blusa_GG': blusa_GG, 'busto_PP': busto_PP, 'busto_P': busto_P, 'busto_M': busto_M, 'busto_G': busto_G, 'busto_GG': busto_GG, 'manga_PP': manga_PP, 'manga_P': manga_P, 'manga_M': manga_M, 'manga_G': manga_G, 'manga_GG': manga_GG, 'modelagem': modelagem, 'height_cm': height_cm})
    else:
        form = ImageForm()
    return render(request, 'clothMeasure2.html')

@login_required(login_url='login')
def results_clothMeasure2(request):
    return render(request, 'results_clothMeasure2.html')