import ast, json

import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse

from a_questions.models import Question
from a_users.models import CustomUser


def home_view(request):
    return render(request, 'home.html')

def survey_view(request, question_id=1):
    questions = Question.objects.all()
    user_id = request.session['user_id']
    session_list = request.session.get('answer_list',[])
    if question_id > questions.count():
        if user_id:
            user = CustomUser.objects.get(pk=user_id)
            user.answer = session_list
            user.save()
            request.session['answer_list'] = []
            request.session.save()
            request.session.modified=True
        return redirect('survey_done_view')
    # 위에 받아온 questions가 있는데... 다른 방법은 없나?
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        # TODO: answer를 처리하는것은 추후에
        answer = request.POST.get('answer')
        session_list.append(int(answer))
        request.session['answer_list'] = session_list
        request.session.modified=True
        # answer = request.POST.get('answer', '') 마지막 ''는 default value
        return redirect(reverse('survey_view', args=(question_id+1,)))

    return render(request, 'survey.html', {'question': question, 'question_id':question_id})

def survey_done_view(request):
    return render(request, 'survey_done.html')



def result_view(request):
    userdata = CustomUser.objects.all().values('ages', 'gender', 'answer')
    questions = Question.objects.all().values('id', 'question_text')

    df_users = pd.DataFrame(list(userdata))
    df_questions = pd.DataFrame(list(questions))

    df_users['answer'] = df_users['answer'].apply(ast.literal_eval)

    summary_data = {}

    for index, question in df_questions.iterrows():
        question_id = question['id']
        question_text = question['question_text']
        calc_index = question_id - 1

        df_users[f'q{question_id}_response'] = df_users['answer'].apply(lambda answers: answers[calc_index])
        grouped_data = df_users.groupby(['gender', 'ages'])[f'q{question_id}_response'].mean().unstack(level=0)

        # DataFrame을 JSON 직렬화 가능한 형태로 변환
        summary_data[question_text] = grouped_data.to_dict('index')

    # 전체 데이터를 JSON 형태로 변환
    df_summary_json = json.dumps(summary_data, ensure_ascii=False)
    return render(request, 'result.html', {'df_summary': df_summary_json})





