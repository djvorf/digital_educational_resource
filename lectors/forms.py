from django import forms

from .models import Reviews, Test, TestQuestions


class ReviewsForm(forms.ModelForm):
    '''Форма отзывов'''
    class Meta():
        model = Reviews
        fields = ("name", "email", "text")


class TestForm(forms.ModelForm):
    '''TTUUT'''
    class Meta():
        models = TestQuestions
        fields = ("name", )