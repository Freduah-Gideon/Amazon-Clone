from django.shortcuts import render
from django.views.generic import View
from .forms import UserCreationForm
from .models import User
from django.core.mail import EmailMessage
from django.http import JsonResponse
# Create your views here.

class RegistrationView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(self.request, 'authentication/base.html', context)

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
                    email = form.cleaned_data.get('email'),
                    first_name = form.cleaned_data.get('first_name'),
                    phone = form.cleaned_data.get('phone')
                )
                user.set_password(password2)
                user.save()
                response['OK'] = 'Check Your Email Address For A Link To Activate Your Account'
                return JsonResponse(response)
        else:
            return JsonResponse(form.errors)


class LoginView(View):
    def get(self):
        pass
    def post(self):
        pass