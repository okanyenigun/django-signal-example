from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):

    def get(self, request):
        #int("asd")
        return render(request, './templates/index.html')
