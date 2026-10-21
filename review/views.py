from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review


def review_list(request):
  reviews = Review.objects.all().order_by('-created_at')
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('review_list')
  else:
    form = ReviewForm()

  return render(
      request, 'review/review_list.html', {'reviews': reviews, 'form': form}
  )



def review_delete(request, pk):
  review = get_object_or_404(Review, pk=pk)
  if request.method == 'POST':
    review.delete()
    return redirect('review_list')

  return render(request, 'review/review_confirm_delete.html', {'review': review})