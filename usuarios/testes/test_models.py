from django .test import TestCase
from ..models import Pessoa

class PessoaTestCase(TestCase):

    def setUp(self):
        Pessoa.objects.create(
            nome = "Franscisco",
            idade = 16
            )

    def test_retorno_str(self):
        p1 = Pessoa.objects.get(nome='Franscisco')

        self.assertEquals(p1.__str__(), 'Franscisco')