from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import FormData


def form_view(request: HttpRequest):
    if request.method == 'POST':
        data = {k: v.strip() for k, v in request.POST.items() if k.startswith('name') and v.strip()}
        if not data:
            return render(request, 'dynamic_form_app/form.html', {
                'error': 'Введите хотя бы одно имя.'})
        FormData.objects.create(data=data)
        return redirect('members_list')
    return render(request, 'dynamic_form_app/form.html')

def members_list(request):
    members = FormData.objects.all().order_by('created_at')
    return render(request, 'dynamic_form_app/members_list.html', {'members': members})    

