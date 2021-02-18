from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def bootstrap_format(fields : dict, float=False):    
    """
    Aplica a classe .form-control nos inputs e o tipo 'date' nos inputs de data
    """
    NON_FORM_CONTROL = ('hidden', 'checkbox')
    def add_widget_attrs(field, value, attr="class"):
        try:
            field.widget.attrs[attr] += " "+value
        except KeyError:
            field.widget.attrs[attr] = value
        return field
    for field in fields:
        try:
            ### Formatação de inputs
            # form-control
            if (fields[field].widget.input_type not in NON_FORM_CONTROL):        
                fields[field] = add_widget_attrs(fields[field], "form-control")
                if float:
                    fields[field] = add_widget_attrs(fields[field], "placeholder", "placeholder")
            # date
            if ('data' in field):
                fields[field].widget.attrs['title'] = "Insira uma data no formato dd/mm/aaaa"
                fields[field].widget.input_type = "date"
            # Interrogação para checkbox
            if (fields[field].widget.input_type == 'checkbox'):
                fields[field] = add_widget_attrs(fields[field], "check-question")
            # Seta em selects
            if (fields[field].widget.input_type == 'select'):
                fields[field] = add_widget_attrs(fields[field], "form-select")
        except AttributeError:            
            continue
    return fields

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields = bootstrap_format(self.fields,True)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password'].label = 'Senha'

        self.error_messages = {
            'inactive': 'Essa conta esta inativa',
            'invalid_login': 'Nome de usuário ou senha inválidos.'
        }
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username']
        labels = {
            'email': ('E-mail'),
            'username': ('Nome de usuário'),
        }

    def __init__(self,*args,**kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields = bootstrap_format(self.fields,True)
        self.fields['username'].help_text = 'Pode conter letras, números e @/./+/-/_ apenas.'
        self.fields['password1'].help_text = 'Minímo de 8 dígitos. Não se esqueça de incluir números, \
            letras MAIÚSCULAS, minúsculas e caracteres especiais -/_/@/+/-.'
        self.fields['password2'].help_text = 'Reescreva a senha anterior para confirmação'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação da Senha'
        self.fields['password1'].widget.attrs.update({
            'minlength': '8',
            'autocomplete': 'new-password',
        })