from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def main(request):
    context = {'message':'Django is great.'}
    return render(request, 'main/main.html', context)

