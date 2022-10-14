from django.shortcuts import render
from ..models.category_model import Category
from django.core.paginator import Paginator

from django.db.models import Count, F, Value, Func
from django.db.models.functions import Length, Upper
from django.db.models.lookups import GreaterThan
from django.db.models import OuterRef, Subquery
from .forms_category import CatalogForm

from django.http import (HttpResponse, HttpResponseRedirect)
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.core.files.base import ContentFile
from django.views.generic import TemplateView

def list(request):
    # pm = Category.objects.all()
    # sort
    # pm = Category.objects.order_by(F('created_at').desc(nulls_last=True)) #.asc()
    # filter
    pm = Category.objects.filter().order_by(F('created_at').desc(nulls_last=True))
    # queryset

    paginator = Paginator(pm, 2)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/view_category.html', {'page_obj':page_obj})

class UploadImage(TemplateView):
    form = CatalogForm
    template_name = 'blog/upload_category.html'

    def post(self, request, *args, **kwargs):
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('catalog:view_upload_template_page', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Upload template
class UploadImageDisplay(DetailView):
    model = Category
    template_name = 'blog/upload_category_display.html'
    context_object_name = 'UF'
