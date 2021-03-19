from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField

class Products(models.Model):
    """
    Model of the products to be exchanged.
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
    created_at = models.DateTimeField(verbose_name=u"Adicionado em",auto_now_add=True, null=True)
    modif_at = models.DateTimeField(verbose_name=u'Última Modificação',auto_now=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'user_pk':self.user.pk, 'pk': str(self.id)})

    def get_badges(self) -> list:
        """Return a list of informations about every badge in troco_por"""
        cat_badge = {
            # cat |   color   |  emoji 
            'LVQ':("#d72c32","📚"),
            'TEC':("#2f2695","💻"),
            'CEE':("#28a6ae","🏠"),
            'EEL':("#5eab16","⚽"),
            'MBA':("#e85d91","👕"),
            'FEM':("#8f5221","🛠"),
            'BRI':("#881186","🤖"),
            'PET':("#874ab0","🐶"),
        }
 
        cat_choices = dict(self.CATEGORY_CHOICES) 
        badges = []
        for cat in self.trocopor.values('category').distinct():
            cat_face = cat_badge.get(cat['category'])
            badge = {'color':cat_face[0], 'icon':cat_face[1],'name':cat_choices[cat['category']]}
            
            badges.append(badge)
        return badges

            
       
def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'products/{0}/{1}'.format(instance.product.id, filename)
class Product_Image(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=product_directory_path)
    
class Troca(models.Model):
    """
    Model that stores information about an ongoin exchange
    """
    STATE_CHOICES = (
        ('A','Troca aceita'),
        ('R','Troca recusada'),
        ('P','Troca pendente')
    )

    product_chosen = models.ForeignKey('Products',related_name="product_chosen" ,on_delete=models.CASCADE, null=False)
    product_to_exchange = models.ForeignKey('Products',related_name="product_to_exchange" ,on_delete=models.CASCADE, null=False)
    finished = models.BooleanField(default=False)
    state = models.CharField(choices=STATE_CHOICES, default='P', max_length=1)

    def __str__(self):
        return self.product_chosen.name+" x "+str(self.product_to_exchange.name)

    
    
    

