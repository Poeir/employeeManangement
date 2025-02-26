from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addUser(request):
    return render(request, 'addUser.html')