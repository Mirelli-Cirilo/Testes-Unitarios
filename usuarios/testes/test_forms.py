from django .test import TestCase
from ..forms import PessoaForm
class PessoaFormTestCase(TestCase):

    def test_pessoa_form_valido(self):
        form = PessoaForm(data={
            'nome':'Mirelli',
            'idade':'17'
        })
        self.assertTrue(form.is_valid())

    def test_pessoa_form_invalido(self):
        form = PessoaForm(data={})
        self.assertFalse(form.is_valid())    