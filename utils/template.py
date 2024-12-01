from django.http import HttpResponse
from django.template import loader

class Template:
    def render(self, request, file, context=None):
        template = loader.get_template(file)
        return HttpResponse(template.render(context, request))