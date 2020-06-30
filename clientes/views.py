from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    template_name = 'listar_clientes.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ClienteListView, self).get_queryset()
        busca = self.request.GET.get('busca')
        if busca:
            queryset = queryset.filter(nomecompleto__icontains=busca)
        return queryset


class ClienteDetailView(DetailView):
    template_name='visualizar_cliente.html'
    queryset = Cliente.objects.all()
    '''
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Cliente, id=id_)'''

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cadastrar_cliente.html"
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')
    success_message = 'Cadastro Realizado com sucesso' 


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cadastrar_cliente.html"
    form_class = ClienteForm
    success_url = '/'
    success_message = "Cadastro atualizado com sucesso."

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "excluir_cliente_confirmacao"
    success_url = reverse_lazy('listar_clientes')




