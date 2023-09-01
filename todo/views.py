from rest_framework import viewsets
from todo.models import TodoList, Pessoa
from todo.serializers import TodoListSerializer, PessoaSerializer

# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer