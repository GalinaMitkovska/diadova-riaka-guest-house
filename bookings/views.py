from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookingEditForm, BookingForm
from .models import Booking


# READ ALL
def booking_list(request):
  bookings = Booking.objects.all()
  return render(request, 'bookings/booking_list.html', {'bookings': bookings})


# READ DETAILS
def booking_detail(request, pk):
  booking = get_object_or_404(Booking, pk=pk)
  return render(request, 'bookings/booking_detail.html', {'booking': booking})


# CREATE
def booking_create(request):
  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save()
      return redirect('booking_detail', pk=booking.pk)
  else:
    form = BookingForm()
  return render(request, 'bookings/booking_form.html', {'form': form})


# UPDATE (с disabled поле във формата)
def booking_edit(request, pk):
  booking = get_object_or_404(Booking, pk=pk)
  if request.method == 'POST':
    form = BookingEditForm(request.POST, instance=booking)
    if form.is_valid():
      form.save()
      return redirect('booking_detail', pk=booking.pk)
  else:
    form = BookingEditForm(instance=booking)
  return render(
      request,
      'bookings/booking_form.html',
      {'form': form, 'is_edit': True},
  )


# DELETE
def booking_delete(request, pk):
  booking = get_object_or_404(Booking, pk=pk)
  if request.method == 'POST':
    booking.delete()
    return redirect('booking_list')
  return render(
      request, 'bookings/booking_confirm_delete.html', {'object': booking}
  )
