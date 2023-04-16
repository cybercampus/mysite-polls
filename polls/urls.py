from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # polls的首页
    path('', views.IndexView.as_view(), name='index'),
    # 显示第三个问题的内容，例如: /polls/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 显示第三个问题的内容回答，例如:: /polls/2/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 显示第三个问题的打分，例如:: /polls/2/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]