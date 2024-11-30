from utils.template import Template

class Views:
    def __init__(self):
        self.template = Template()

    def home(self, request):
        return self.template.render(request, 'home.html')

    def about(self, request):
        return self.template.render(request, 'about.html')
