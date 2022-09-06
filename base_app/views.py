import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base_app.form import RegistrationForm, AccountAuthenticationForm, ResCa, ResFin, ResInf, Rl1Form, Rl2Form
# from base.form import RoleForm
from .models import  RL1, RL2, GeneralDTable, RchA, RespoINf, customuser
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def loginPage(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            role = request.POST['role']
            password = request.POST['password']
            user = authenticate(email=email,role = role, password=password)
            if user:

                login(request, user)

            # try:
                # user = Base.objects.get(email=email , role=role)
                user_role = user.role
                print(user.username)

                if user_role == "chargee affaire":
                    return redirect('respo_ca')
                elif user_role == "responsable informatique":
                    return redirect('respo_info')
                elif user_role == "responsable financier":
                    return redirect('respo_fin')
                elif user_role == "responsable logistique1":
                    return redirect('respo_log1')
                elif user_role == "responsable logistique2":
                    return redirect('respo_log2')
                
               
            # except:

            #     form = AccountAuthenticationForm()
                 
            #     context['login_form'] = form
            #     return render(request, 'base/login.html', context)

    else:
       form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# def login_view(request):

# 	context = {}

# 	user = request.user
# 	if user.is_authenticated: 
# 		return redirect("home")

# 	if request.POST:
# 		form = AccountAuthenticationForm(request.POST)
# 		if form.is_valid():
# 			email = request.POST['email']
# 			password = request.POST['password']
# 			user = authenticate(email=email, password=password)

# 			if user:
# 				login(request, user)
# 				return redirect("home")

# 	else:
# 		form = AccountAuthenticationForm()

# 	context['login_form'] = form

# 	# print(form)
# 	return render(request, "account/login.html", context)
















































def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, role=role, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'base/register.html', context)

def home(request):
    return render(request, 'base/home.html')

def rl1Page(request):

    user_log1 = RL1.objects.all()
    context = {'user_log1':user_log1}

    if request.POST:
        form = Rl1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rl1_form'] = form
    else:  # GET request
        form = Rl1Form()
        context['rl1_form'] = form
    return render(request, 'base/home.html', context)

def rl2Page(request):
    user_log2 = RL2.objects.all()

    context = {'user_log2' : user_log2}

    if request.POST:
        form = Rl2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rl2_form'] = form
    else:  # GET request
        form = Rl2Form()
        context['rl2_form'] = form
    return render(request, 'base/home.html', context)


def rinfoPage(request):
    user_info = ResInf.objects.all()
    context = {'user_info' : user_info}

    if request.POST:
        form = ResInf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rinf_form'] = form
    else:  # GET request
        form = ResInf()
        context['rinf_form'] = form
    return render(request, 'base/home.html', context)


def rfinPage(request):
    user_fin = ResFin.objects.all()
    context = {'user_fin' : user_fin}    

    if request.POST:
        form = ResFin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rfin_form'] = form
    else:  # GET request
        form = ResFin()
        context['rfin_form'] = form
    return render(request, 'base/home.html', context)


@login_required(login_url='/login')
def RCa(request):
    user_ca = RchA.objects.all()
    context = {'user_ca' : user_ca}

    return render(request, 'base/respo_ca.html', context)



def addRCa(request):
    
    form = ResCa()

    if request.method == 'POST':
        form = ResCa(request.POST)
        if form.is_valid():
            resca =form.save(commit=False)
            resca.save()
            return redirect('home')
        
    context={'form': form}
    return render(request, 'base/respo_ca_add.html', context)

# def hideRcaAction(request, pk):
#     user_role = RchA.objects.get(id=pk)
#     context = {'obj' : user_role}
#     return render(request, 'base/hide_respo_ca.html', context)


def General_db(request):
    general_datable = GeneralDTable.objects.all()
    context = {'general_datable' : general_datable}
    print(general_datable)

    return render(request, 'base/home.html', context)