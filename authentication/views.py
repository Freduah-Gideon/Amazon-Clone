from django.shortcuts import render,reverse
from django.views.generic import View
from .forms import UserCreationForm,UserLoginForm
from .models import User
from django.core.mail import EmailMessage
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib import auth
# Create your views here.

response = {}
class RegistrationView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(self.request, 'authentication/register.html', context)

    def post(self, request):
        response = {}
        form = UserCreationForm(self.request.POST or None)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                response['password'] = 'Passwords Do Not Match'
                return JsonResponse(response)
            else:
                user = User.objects.create_user(
                    email=form.cleaned_data.get('email'),
                    first_name=form.cleaned_data.get('first_name'),
                    phone=form.cleaned_data.get('phone')
                )
                user.set_password(password2)
                user.save()
                response['OK'] = 'Check Your Email Address For A Link To Activate Your Account'
                return JsonResponse(response)
        else:
            return JsonResponse(form.errors)


class LoginView(View):
    def get(self,request):
        form = UserLoginForm()
        context = {
            form: form
        }
        return render(self.request, 'authentication/login.html',context)

    def post(self,request):
        print(self.request.POST)
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(self.request,user)
            response['OK'] = reverse('product:home')
            return JsonResponse(response)
        else:
            response['error'] = 'Invalid Credentials'
            return JsonResponse(response)
        # except:
        #     response['error'] = 'It Skipped The Try Block'
        #     return JsonResponse(response)