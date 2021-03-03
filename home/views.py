from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student, User
from django.views.generic import View, TemplateView,ListView, DetailView, CreateView, UpdateView
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required, login_required



# Create your views here.
@login_required
def home_view(request):
    return render(request, 'dashboard.html')

@login_required
def add_student_form_view(request):
    if request.method=='POST':
        form = ('first_name', 'last_name', 'adhar', 'dob', 'father', 'mother', 'class', 'section', 'lang', 'phone', 'address', 'email')
        elements = [request.POST.get(x) for x in form]
        print(elements)
    return render(request, 'add_student.html')


@login_required
def list_student_view(request):
    if request.user.has_perm('user.view_student'):
        all_students = User.objects.all().filter(type='1', is_active=True)
        return render(request, 'list_student.html', {'students':all_students})
    else:
        return render(request, 'access_denied.html', status=404)

@login_required
def perm(request):
    a=request.user.get_group_permissions()
    print(a)

    return HttpResponse(a)

class StudentView(TemplateView):
    template_name = "sample2.html"
    form_class = StudentForm
    initial ={'key':'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        pk = self.kwargs['pk']
        
        return render(request, self.template_name, {'form': form, 'pk':pk})


class StudentUpdateView(View):
    template_name = "edit_student.html" 
    # DetailView
    def get_object(self):
        id = str(self.kwargs.get('id'))
        user = User.objects.get(username=id)
        pk=user.pk
        obj = None
        if id is not None:
            obj = get_object_or_404(Student, user_id=pk)
        return obj
    
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = StudentForm(instance=obj)
            context['object'] = obj
            context['form'] = form
            
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = StudentForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                print(True)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)








