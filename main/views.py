from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	dog_image = requests.get('https://dog.ceo/api/breeds/image/random').json()
	dog_fact = requests.get('http://dog-api.kinduff.com/api/facts').json()
	return render(request, 'index.html', {'dog_fact':dog_fact, 'dog_image':dog_image})
