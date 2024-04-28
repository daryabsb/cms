from django.shortcuts import render

# Create your views here.



def crm_index(request):
    return render(request, 'crm/index.html', {'title': 'CRM'})