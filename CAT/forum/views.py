from django.shortcuts import render,redirect
from .models import Question
from .forms import QuestionForm
import datetime

def index(request):
	questions=Question.objects.all()
	return render(request,'index.html',{'questions':questions})

def get_query(request):
	if request.method == 'POST':
		#Creating a form instance for dealing with a form
		form = QuestionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			# post.question=request.question
			post.save()
			return redirect('/success/')
	else:
		form=QuestionForm()
	return render(request,'query_forum.html',{'form':form})

def success(request):
	return render(request,'success.html',{})