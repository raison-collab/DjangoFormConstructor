from typing import Type

from django import forms
from django.forms import modelform_factory
from . import models


def create_form(form_model: models.Form) -> Type[forms.Form]:
    """
    Создает форму на основе модели, где писана форма и ее поля
    :param form_model: модель
    :return: форму
    """
    form_attrs = {}

    for field_model in form_model.fields.all():

        field_type = field_model.type
        field_params = {
            'label': field_model.name,
            'required': field_model.required,
        }
        if field_model.max_length:
            field_params['max_length'] = field_model.max_length

        field = getattr(forms, field_type)(**field_params)

        form_attrs[field_model.name] = field
    # Создаем класс формы
    form_class = modelform_factory(models.Form, fields='__all__', form=forms.Form)

    # добавляем поля в форму
    form_class.base_fields = form_attrs

    return form_class
