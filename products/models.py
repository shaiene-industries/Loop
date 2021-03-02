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

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name+" | by "+str(self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('products:productDetail', kwargs={'pk': str(self.id)})

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
 
        badges = []
        for cat in self.trocopor.all():
            cat_face = cat_badge.get(cat.category)
            badge = {'color':cat_face[0], 'icon':cat_face[1],'name':cat.get_category_display()}
            
            badges.append(badge)
        return badges

            
       
def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'products/{0}/{1}'.format(instance.product.id, filename)
class Product_Image(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=product_directory_path)
    
    



    
    
    

