from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView
from .models import BaseRegisterForm
from protect.models import User


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name = 'authors')
    if not request.user.groups.filter(name = 'authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')



class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code = request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request,'user/invalid_code.html')
        return redirect('account_login')