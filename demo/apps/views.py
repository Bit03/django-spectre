from django.views import generic


class DemoView(generic.TemplateView):
    template_name = 'demo.html'

