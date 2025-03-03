from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

def scrape(request):
    page = requests.get('https://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    # link_address = []
    # for link in soup.find_all('a'):
    #     link_address.append(link.get('href'))

    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        Link.objects.create(address=link_address, name=link_text)

    data = Link.objects.all()

    # return render(request, 'myapp/result.html', {'link_adress': link_address})
    return render(request, 'myapp/result.html', {'data': data})