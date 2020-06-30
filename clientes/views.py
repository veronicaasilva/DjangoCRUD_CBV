from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente
from .forms import ClienteForm


class ClienteListView(LoginRequiredMixin, ListView):
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


class ClienteDetailView(LoginRequiredMixin, DetailView):
    template_name='visualizar_cliente.html'
    queryset = Cliente.objects.all()


class ClienteCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "cadastrar_cliente.html"
    form_class = ClienteForm
    success_message = ('Cliente cadastro com sucesso!')
    success_url = reverse_lazy('listar_clientes')
    
    

class ClienteUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "cadastrar_cliente.html"
    form_class = ClienteForm
    success_message = 'Cadastro alterado com sucesso' 
    success_url = reverse_lazy('listar_clientes')
    

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "excluir_cliente_confirmacao.html"
    success_url = reverse_lazy('listar_clientes')
    


def clonar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.pk = None
    cliente.save()
    messages.success(request,  'Cliente clonado com sucesso!') 
    return redirect('listar_clientes')



