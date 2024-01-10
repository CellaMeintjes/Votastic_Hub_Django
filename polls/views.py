from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Get questions and display them


def index(request):
	"""
    Get questions and display them.

    :param request: HttpRequest object
    :return: Rendered HTML page displaying the latest questions
    """
	latest_question_list = Question.objects.order_by('id')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# Show specific question and choices


def detail(request, question_id):
	"""
    Show specific question and choices.

    :param request: HttpRequest object
    :param question_id: ID of the question to display
    :return: Rendered HTML page displaying the details of a specific question
    """
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

# Get question and display results


def results(request, question_id):
	"""
    Get question and display results.

    :param request: HttpRequest object
    :param question_id: ID of the question to display results for
    :return: Rendered HTML page displaying the results of a specific question
    """
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
	"""
    Vote for a question choice.

    :param request: HttpRequest object
    :param question_id: ID of the question to vote for
    :return: HttpResponseRedirect to the results page after voting
    """
	
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))
