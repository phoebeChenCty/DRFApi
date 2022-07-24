from multiprocessing import context
from django.shortcuts import render
from django.views import View


class ChangeFruitView(View):
    def get(self, request):
        times = request.GET.get('times')
        context = {'rest_times': int(times)-1}
        return render(request, 'bigmelon/changeFruit.html', context=context)
