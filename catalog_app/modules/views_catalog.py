from django.views.generic import TemplateView, DetailView

class CatalogView(TemplateView):
    # model = Author
    # from pprint import pprint; pprint('author')
    context_object_name = 'catalog'
    template_name = 'home_catalog.html'