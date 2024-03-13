from pprint import pprint
from typing import Type

from django.core.handlers.wsgi import WSGIRequest
from django.forms import forms
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import create_form
from .models import Form


# Create your views here.
def index(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hello")


@csrf_exempt
def form_view(request: HttpRequest, form_id: int) -> HttpResponse:

    form_model: Form = get_object_or_404(Form, id=form_id)

    form_class: Type[forms.Form] = create_form(form_model)

    if request.method == 'POST':
        form: forms.Form = form_class(request.POST)

        pprint(form.errors)

    else:
        form: forms.Form = form_class()

    return render(request, 'MainApp/form.html', {'form': form})
