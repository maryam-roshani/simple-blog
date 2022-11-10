from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required

def book_list(request):
	books = Book.objects.all().order_by('name') 
	return render(request, 'myApp/book_list.html', {'books' : books} )


@login_required(login_url='/accounts/login/')
def book_create(request):
	if request.method == 'POST':
		form = forms.BookForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.reader = request.user
			instance.save()
			return redirect( 'myApp:list')
	else:
		form = forms.BookForm()
	return render(request, 'myApp/book_creation.html', {'form' : form} )

def book_detail(request, slug ):
	book = Book.objects.get(slug=slug) 
	return render(request, 'myApp/book_detail.html', {'book' : book} )



