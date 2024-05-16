from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm ,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.contrib import messages
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class LogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return super().get(request, *args, **kwargs)


class UserBankAccountUpdateView(View):
        template_name = 'accounts/user_registration.html'

        def get(self,request):
            form = UserUpdateForm(instance=request.user)
            return render(request,self.template_name,{'form':form})
        
        
        def post(self,request):
            form = UserUpdateForm(request.POST,instance= request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
            return render(request,self.template_name,{'form':form})