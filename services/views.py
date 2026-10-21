from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ServiceForm
from .models import Service


# READ
def service_list(request):
  services = Service.objects.all()
  return render(request, 'services/service_list.html', {'services': services})


# CREATE
def service_create(request):
  if request.method == 'POST':
    form = ServiceForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('service_list')
  else:
    form = ServiceForm()
  return render(
      request,
      'services/service_form.html',
      {'form': form, 'title': 'Добави услуга'},
  )


# UPDATE
def service_edit(request, pk):
  service = get_object_or_404(Service, pk=pk)
  if request.method == 'POST':
    form = ServiceForm(request.POST, instance=service)
    if form.is_valid():
      form.save()
      return redirect('service_list')
  else:
    form = ServiceForm(instance=service)
  return render(
      request,
      'services/service_form.html',
      {'form': form, 'title': 'Редактирай услуга'},
  )


# DELETE
def service_delete(request, pk):
  service = get_object_or_404(Service, pk=pk)
  if request.method == 'POST':
    service.delete()
    return redirect('service_list')
  return render(
      request, 'services/service_confirm_delete.html', {'object': service}
  )
