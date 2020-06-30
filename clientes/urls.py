from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, clonar_cliente

urlpatterns = [
   path('', ClienteListView.as_view(), name='listar_clientes'),
   path('<int:pk>/visualizar', ClienteDetailView.as_view(), name='visualizar_cliente'),
   path('cadastrar_cliente', ClienteCreateView.as_view(), name='cadastrar_cliente'),
   path('<int:pk>/atualizar', ClienteUpdateView.as_view(), name='atualizar_cliente'),
   path('<int:pk>/excluir', ClienteDeleteView.as_view(), name='deletar_cliente'),
   path('clonarcadastro/<int:pk>', clonar_cliente, name='clonarcadastro'),
]