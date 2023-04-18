from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #返回最后发布的5个问题
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        #排除没有发布的问题
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'result.html'

'''
#定义视图函数
def index(request):
    return HttpResponse("你好，这里是第一个 Django 页面！")

#从数据库里查找最新发布的5个问题
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

#通过模板语言的变量进行传递信息
def index(request):
    context = {'title':'我的站点' ,'first_name': '乙丙', 'last_name': '白'}
    return render(request, 'index.html', context)

#从数据库中读取数据，传递给模板
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)

#根据 id 返回一个问题的详细信息
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#从数据库中读取数据，传递给模板
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

#根据问题 id 返回问题的回答
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})

#根据问题题 id 返回问题的打分
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 刷新form页面
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 在成功处理 POST 数据后，返回一个 HttpResponseRedirect 刷新页面。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
