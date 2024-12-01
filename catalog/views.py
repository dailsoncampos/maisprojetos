from utils.template import Template

class Views:
    def __init__(self):
        self.template = Template()

    def catalog(self, request):
        return self.template.render(request, 'index.html', {'content': 'Catálogo'})
