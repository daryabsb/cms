from django.shortcuts import render, redirect,get_object_or_404
from django.utils.translation import gettext_lazy as _
from src.dashboard.forms import ConfigurationForm
from src.dashboard.models import Configurations

from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

from src.dashboard import setup_config
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required 
import pickle
import mimetypes


@login_required(login_url='login')
def index(request):
    print("This view is called!")
    context={
        "page_title":"Dashboard",
        "host":"Host",
    }
    return render(request,'dashboard/index.html',context)


@login_required(login_url='dashboard:login')
@permission_required({'dashboard.view_configurations','dashboard.delete_configurations'}, raise_exception=True)
def deleteConfigSlider(request,id,file_name):
    file_path = '/media/Configurations/'+file_name
    config_obj = Configurations.objects.get(id=id)
    if config_obj:
        path_list = config_obj.value.split(',')
        path_list.remove(file_path)
        config_obj.value = ','.join(path_list)
        config_obj.save()
        prefix = config_obj.name.split('.')[0]
    else:
        messages.warning(request,"Configurations Not Found")
        return redirect("dashboard:all-config")

    return redirect(f'/dashboard/configurations/prefix/{prefix}')