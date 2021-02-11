from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

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

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, required=True)
    password = forms.CharField(label="Password", max_length=128, required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = ['username','password']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password','username','email']

    def __init__(self,*args,**kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields = bootstrap_format(self.fields,True)
        self.fields['username'].help_text = 'Pode conter letras, números e @/./+/-/_ apenas.'
        self.fields['password'].help_text = 'Minímo de 8 dígitos. Não se esqueça de incluir números, \
            letras MAIÚSCULAS, minúsculas e caracteres especiais -/_/@/+/-.'

    def clean(self):
       for field, value in self.cleaned_data.items():
           self.cleaned_data['field'] = value.lower()