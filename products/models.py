from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

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
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name + " | by " + str(self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('products:productDetail', kwargs={'pk': str(self.id)})

    
    
class TrocoPor(models.Model):
    """
    Modelo de relação muitos pra muitos da tabela Produto com ela mesma.
    Delimita os exemplos de produtos (campo: exemplo) que poderiam ser trocados
    pelo produto delimitado (campo: produto).
    """
    produto = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='produto_id')
    exemplo = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='exemplo_id')


    
    
    

