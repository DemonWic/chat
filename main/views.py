from django.shortcuts import render
from account.models import Account
#from main.models import Question
def home_screen_view(request):


  #вариант1
  #context = {}
  #context['some_string'] = "Что-то , что положу во вью"
  #context['some_number'] = 5677

  #вариант2
  #context = {
    #'some_string': "Что-то , что положу во вью",
    #'some_number': 5677,

  #}
  #list_of_values = []
  #list_of_values.append("первый")
  #list_of_values.append("второй")
  #list_of_values.append("третий")
  #list_of_values.append("четвертый")
  #context['list_of_values'] = list_of_values
  # questions = Question.objects.all()
  # context['questions'] = questions
  
  context = {}
  accounts = Account.objects.all()
  context['accounts'] = accounts


  return render(request, 'main/home.html', context)
