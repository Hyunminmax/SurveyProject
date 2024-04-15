from django.shortcuts import render, redirect, get_object_or_404
from a_questions.models import Question
from django.urls.base import reverse


def home_view(request):
    return render(request, 'home.html')

def survey_view(request, question_id=1):
    questions = Question.objects.all()
    if question_id > questions.count():
        return redirect('survey_done_view')
    # 위에 받아온 questions가 있는데... 다른 방법은 없나?
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        # TODO: answer를 처리하는것은 추후에
        answer = request.POST.get('answer')
        # answer = request.POST.get('answer', '') 마지막 ''는 default value
        return redirect(reverse('survey_view', args=(question_id+1,)))

    return render(request, 'survey.html', {'question': question, 'question_id':question_id})

def survey_done_view(request):
    return render(request, 'survey_done.html')