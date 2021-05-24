from django.shortcuts import render

# Create your views here.


def client_view(request):
    return render(request, 'index.html')

