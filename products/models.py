from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField

class Products(models.Model):
    """
    Modelo dos produtos que serão trocados no site.
    """

    CATEGORY_CHOICES = (
        ('LVQ','Livros, Revistas e Quadrinhos'),
        ('TEC','Tecnologia'),
        ('CEE', u'Casa e Eletrodomésticos'),
        ('EEL','Esporte e Lazer'),
        ('MBA', u'Moda, Bijuterias e Acessórios'),
        ('FEM', u'Ferramentas e Máquinas'),
        ('BRI', u'Brinquedos Infantis'),
        ('PET', u'Pets'),
    )

    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=3,choices=CATEGORY_CHOICES)
    info = MarkdownxField()
    trocopor = models.ManyToManyField("self", blank=True, symmetrical=False)
    data_criacao = models.DateTimeField(verbose_name=u"Adicionado em",auto_now_add=True, null=True)
    data_modif = models.DateTimeField(verbose_name=u'Última Modificação',auto_now=True, null=True)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name + " | by " + str(self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('products:productDetail', kwargs={'pk': str(self.id)})

    
    



    
    
    

