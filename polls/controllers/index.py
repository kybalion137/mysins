from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.forms import UserForm
from django.utils import timezone
from django.views.generic import ListView

#from django.views.generic.list import ListView
from ..models import Tishki


def index(request):
    tishki = Tishki.objects.all()

    return render(request, 'index.html', {"tishki": tishki})


def futba1(request):
    return render(request, 'futba1.html', {})


def futba2(request):
    return render(request, 'futba2.html', {})


def futba3(request):
    return render(request, 'futba3.html', {})

def onas(request):
    return render(request, 'onas.html', {})

def oplata(request):
    return render(request, 'oplata.html', {})


def sale(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = request.POST.get("age")
            return HttpResponse(f"<h2>Возрадуйся и возмолись, {name}, ибо на {age} год своей жизни ты наконец обрел верный путь. <br> Добро пожаловать в семью ФИР.</h2>")
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "sale.html", {"form": userform})


#class Tiskiviews(ListView):
class TishkiListView(ListView):

    model = Tishki
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


