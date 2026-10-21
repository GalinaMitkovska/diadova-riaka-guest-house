from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from rooms.forms import RoomForm
from rooms.models import Room

def room_list(request):
  rooms = Room.objects.all()
  return render(request, 'rooms/room_list.html', {'rooms': rooms})



def room_create(request):
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('room_list')
  else:
    form = RoomForm()
  return render(
      request, 'rooms/room_form.html', {'form': form, 'title': 'Добави стая'}
  )



def room_edit(request, pk):
  room = get_object_or_404(Room, pk=pk)
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save()
      return redirect('room_list')
  else:
    form = RoomForm(instance=room)
  return render(
      request,
      'rooms/room_form.html',
      {'form': form, 'title': 'Редактирай стая'},
  )



def room_delete(request, pk):
  room = get_object_or_404(Room, pk=pk)
  if request.method == 'POST':
    room.delete()
    return redirect('room_list')
  return render(
      request, 'rooms/room_confirm_delete.html', {'object': room}
  )