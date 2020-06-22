from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_tasks=List.objects.all
			return render(request, 'home.html', {'all_tasks': all_tasks})

	else:
		all_tasks=List.objects.all
		return render(request, 'home.html', {'all_tasks': all_tasks})

	


def delete(request, key):
	tag=List.objects.get(pk=key)
	tag.delete()
	return redirect('home')



def edit(request, key):

	if request.method == 'POST':
		task=List.objects.get(pk=key)

		form = ListForm(request.POST or None, instance=task)

		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		task=List.objects.get(pk=key)
		return render(request, 'edit.html', {'task': task})
