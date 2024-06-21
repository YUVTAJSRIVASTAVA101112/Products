# from django.db import models
# from django.contrib.auth.models import User
# from product1.models import Product

# # Create your models here.

# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username

    

# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()

#     def __str__(self):
#         return self.name
    
# # product list

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='salesapp/static/media/')

#     def __str__(self):
#         return self.name

# # gown list 

# class Gown(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='salesapp/static/media/')

#     def __str__(self):
#         return self.name

# # accessories

# class Accessories(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='salesapp/static/media/')

#     def __str__(self):
#         return self.name
    
# #birthday


# class Birthdays(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='salesapp/static/media/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

# #casuals

# class Casuals(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='salesapp/static/media/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name
    
# # ethnic

# class Ethnics(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='salesapp/static/media/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name
    
# #mom_daughter



# class Mom_daughters(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='salesapp/static/media/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name
    
# #Parties
# class  Parties(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='salesapp/static/media/')
#     price = models.DecimalField(max_digits=8, decimal_places=2)

#     def _str_(self):
#         return self.name
    

# #cart

# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Cart ({self.id}) for {self.user}'

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'
    


# class Cart(models.Model):


#     def get_total_price(self):
#         return sum(item.product.price * item.quantity for item in self.items.all())

from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
# Product list

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sales/static/media/')

    def __str__(self):
        return self.name

# Gown list 

class Gown(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sales/static/media/')

    def __str__(self):
        return self.name

# Accessories

class Accessories(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sales/static/media/')

    def __str__(self):
        return self.name
    
# Birthdays

class Birthdays(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sales/static/media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Casuals

class Casuals(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sales/static/media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# Ethnics

class Ethnics(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sales/static/media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# Mom_daughters

class MomDaughters(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sales/static/media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# Parties

class Parties(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sales/static/media/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    

# Cart

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart ({self.id}) for {self.user}'

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
