from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Lector
from .forms import ReviewsForm


class MainPage(ListView):
    '''Список лекций'''
    model = Lector
    queryset = Lector.objects.all()
    template_name = "lectors/index1.html"

    def post(self, request):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=True)
        return redirect("/")


class LectorsViews(ListView):
    '''Список лекций'''
    model = Lector
    queryset = Lector.objects.filter(draft=False)
    template_name = "lectors/lectors.html"


class LectorDetailViews(DetailView):
    '''Список лекций'''
    model = Lector
    slug_field = "url"
