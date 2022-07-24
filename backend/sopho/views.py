from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View


class ChangeFruitView(View):
    def get(self, request):
        times = request.GET.get('times')
        context = {'rest_times': int(times)-1}
        return render(request, 'bigmelon/changeFruit.html', context=context)


class GameOverView(View):
    def get(self, request):
        win = request.GET.get('win')
        ordered = False
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
