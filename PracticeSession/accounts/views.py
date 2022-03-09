from django.shortcuts import render,redirect
from  django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()
from .forms import MyForm


def login(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print("success")
            messages.info(request, "Valid")
        else:
            print("fail")
            messages.info(request, "InValid")
            return redirect('login')

        username = request.POST['username']
        date_of_birth = request.POST['date_of_birth']

        user = auth.authenticate(username=username,password=date_of_birth)

        if user is not None:
            auth.login(request,user)
            if user.staff_user == 1:
                return render(request, 'staff.html')
            elif user.student_user == 1:
                return render(request, 'student.html')
            elif user.student_user == 0 and user.staff_user == 0:
                return render(request, 'parent.html')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    else:
        form = MyForm()
        return render(request, "login.html", {"form": form})
        records = User.objects.all()
        return render(request, 'staff.html', {'rec': records})
        return render(request, 'student.html', {'rec': records})
        return render(request, 'parent.html', {'rec': records})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        username = request.POST['username']
        email = request.POST['email']
        choice = request.POST.get('user_type',"off")
        date_of_birth = request.POST['date_of_birth']

        print(choice)

        if User.objects.filter(username=username).exists():
            #print("Username already taken")
            messages.info(request,'Username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            #print("Email already taken")
            messages.info(request, 'Email already taken')
            return redirect('register')
        else:
            if choice == "staff":
                staff_user = True
                student_user = False
            elif choice == "student":
                student_user = True
                staff_user = False
            else:
                student_user = False
                staff_user = False
            user = User.objects.create_user(username=username,password=date_of_birth,email=email,first_name=first_name,last_name=last_name,middle_name=middle_name,date_of_birth=date_of_birth,staff_user=staff_user,student_user=student_user)
            user.save();
            #print('user created')
            return redirect('login')


        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
