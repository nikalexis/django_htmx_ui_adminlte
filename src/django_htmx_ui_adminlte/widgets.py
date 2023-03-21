from django.forms.widgets import Input, ClearableFileInput


class SliderInput(Input):
    template_name = 'django/forms/widgets/slider.html'


class ImageInput(ClearableFileInput):
    template_name = 'django/forms/widgets/image.html'
