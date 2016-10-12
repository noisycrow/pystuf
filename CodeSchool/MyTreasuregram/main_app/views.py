from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
#    name = 'Gold Nugget'
#    value = 1000.00
#    context = {'treasure_name': name, 'treasure_val': value}
#    return render(request, 'index.html', context)
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

"""
class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",""),
    Treasure("Fool's Gold", 0, "pyrite", "Fool's Falls, CO",""),
    Treasure("Coffee Can", 20.00, 'tin', "Acme, CA","")
]
"""