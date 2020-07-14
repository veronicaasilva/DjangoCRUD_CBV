from django.test import TestCase
from model_mommy import mommy

class ClienteTestCase(TestCase):
    
    def setUp(self):
        self.cliente = mommy.make('Cliente')
    
    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nomecompleto)