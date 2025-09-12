from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import login


# Create your views here.
@permission_required('app_name.can_edit', raise_exception=True)
def my_view(request):
    return render(request, 'index.html')
