from django.shortcuts import render
from user.models import User, Student
from .forms import UserRegisterForm
import random
import array
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Group
from .forms import StudentAddForm

def user_generator():
  last_user = User.objects.all().order_by('id').last()
  last_username = last_user.username
  new_username = int(last_username) + 1
  return new_username

def  pass_generator():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    return password

def createUser(type, group):
    r_form = UserRegisterForm()
    user = r_form.save(commit=False) # Holds the data 
    username = user_generator()
    password = pass_generator()
    user.username = username
    user.set_password(password) # creates text into hash
    user.type = type
    user.save()

    group = Group.objects.get(name=group)
    user.groups.add(group)
    con = {'userid':username, 'password':password, 'occupancy':type}
    return con

adminPermissions = ['user.view_user', 'user.add_user', 'user.change_user']

@login_required
@permission_required(adminPermissions)
def create_student(request):
    form = StudentAddForm(request.POST or None)
    if form.is_valid():
        
        input_val = ['first_name', 'last_name', 'adhar', 'dob', 'father', 'mother', 'class', 'section', 'lang', 'phone', 'address', 'email']
        context = createUser('1', 'student')
        user = User.objects.get(username=context['userid'])
        xuser = Student.objects.create(user=user)
        xuser.save()

        form = StudentAddForm(request.POST or None, instance=user)
        form.save()
        return render(request, "add_student.html", {'form':form})
    return render(request, 'add_student.html', {'form':form})


@login_required
def create_professor(request):
    context = createUser(2, 'professor')
    return render(request, "sample.html", context)

@login_required
def create_admin(request):
    context = createUser(3, 'admin')
    return render(request, "sample.html", context)


# @login_required
# def add_student_form_view(request):
#     if request.method=='POST':
#         input_val = ['first_name', 'last_name', 'adhar', 'dob', 'father', 'mother', 'class', 'section', 'lang', 'phone', 'address', 'email']
#         add_form = StudentAddForm()
#         student = add_form.save(commit=False)
#         for x in input_val:
#             student.x = request.get(x)
#         print(student)
#     return render(request, 'add_student.html')