from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            return redirect(reverse('home'))  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'newsapi/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    
    return render(request, 'newsapi/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout




API_KEY='2e094fbde9234989923b7f432902973b'


@login_required
def home(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')
        language = request.GET.get('language', '')
        category = request.GET.get('category', '')
        sources = request.GET.get('sources', '')
        from_date = request.GET.get('from_date', '')
        to_date = request.GET.get('to_date', '')

        refresh = request.GET.get('refresh')

        

        # Initialize the articles list
        articles = []

        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])


        if refresh:
            url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])


        if keyword:
            url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])

        if category:
            url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])

        if language:
            url = f'https://newsapi.org/v2/everything?q=all&language={language}&apiKey={API_KEY}'

            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])

        if from_date and to_date:
            url = f'https://newsapi.org/v2/everything?q=all&from={from_date}&to={to_date}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])


        context = {
            'articles': articles,
            'keyword': keyword,
            'language': language,
            'category': category, 
             'sources':sources,
            'user': request.user
        }

        return render(request, 'newsapi/home.html', context)

    return render(request, 'newsapi/home.html', {})



