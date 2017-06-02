from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') + HttpResponse 이 과정을 줄인 게 render 함수
    # get_list_or_404를 사용한 경우
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id가 pk인 Question객체를 가져와
    # context라는 이름을 가진 dict에 'question'이라는 키 값으로 위 변수를 전달
    # 이후 'polls/detail.html'과 context를 렌더한 결과를 리턴

    # question.choice_set = Choice.objects.filter(question=question)

    # polls/detail에서 해당 question의 question_text를 출력
    # try:
    #     question = Question.objects.get(pk=question_id)  # get(쿼리셋에서 어떤 것을 집어오는 것)함수는 pk값을 받는다 !
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)  # 오류 검사 한 줄로 줄여쓴 것
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    # question_id가 pk인 Question객체를 가져와
    # context라는 이름을 가진 dict에 'question'이라는 키 값으로 위 변수를 전달
    # 이후 'polls/detail.html'과 context를 렌더한 결과를 리턴
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # request의 method가 POST방식일 때,
    # 전달받은 데이터 중 'choice'키에 해당하는 값을
    # HttpResponse에 적절히 돌려준다

    # choice키에 해당하는 Choice인스턴스의 vote값을 1증가시키고
    # 데이터베이스에 변경사항을 반영
    # 이후  results페이지로 redirect
    if request.method == 'POST':
        date = request.POST
        try:
            choice_id = date['choice']

            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            # return HttpResponse('Choice is %s' % choice_id)

            # 이후 results페이지로 redirect
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            # message 프레임워크를 사용
            # 지금 몰라도 됨
            # request에 메시지를 저장하고 
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
            return redirect('polls:detail', question_id)
    else:
        return HttpResponse("You're voting on question %s." % question_id)
