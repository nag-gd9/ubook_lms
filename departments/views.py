from django.shortcuts import render
from django.views.generic import CreateView
from .models import Department
from .forms import DepartmentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = "sample2.html"
    success_url = '/department/'


