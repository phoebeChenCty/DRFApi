from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from .serializers import CakeSerializer
from .models import Cake


class ChangeFruitView(View):
    def get(self, request):
        times = request.GET.get('times')
        context = {'rest_times': int(times)-1}
        return render(request, 'bigmelon/changeFruit.html', context=context)


class GameOverView(View):
    def get(self, request):
        win = request.GET.get('win')
        model_data = Cake.objects.first()
        ordered = (model_data.title != "Undefined")
        if win == 'false' and not ordered:
            return redirect('nono')
        if win == 'true' and not ordered:
            return redirect('order')

        context = {'win': win == 'true'}
        return render(request, 'bigmelon/gameover.html', context=context)


class GameOverNoNoView(View):
    def get(self, request):
        return render(request, 'bigmelon/nono.html')


class GameOverOrderView(View):
    def get(self, request):
        return render(request, 'bigmelon/order.html')

    def post(self, request):
        for title in ['c1', 'c2']:
            if title in request.POST:
                print(title)
                cake = Cake.objects.first()
                cake.title = title
                cake.save()
                context = {'win': True}
                return render(request, 'bigmelon/gameover.html', context=context)


class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
