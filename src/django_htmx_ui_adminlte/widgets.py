# from django.forms import Widget
from django.forms.widgets import TextInput, Input, ClearableFileInput


class SliderInput(Input):
    template_name = 'django/forms/widgets/slider.html'


class ImageInput(ClearableFileInput):
    template_name = 'django/forms/widgets/image.html'


class MarkdownWidget(TextInput):
    template_name = 'django/forms/widgets/markdown.html'

