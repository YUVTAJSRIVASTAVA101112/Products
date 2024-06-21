# from django.contrib import admin
# from .models import User
# from .models import Product,Gown,Accessories,Birthdays,Casuals,Ethnics,Mom_daughters,Parties,Cart,CartItem

# admin.site.register(User) 

# # product list

# admin.site.register(Product)

# admin.site.register(Gown)

# admin.site.register(Accessories)

# admin.site.register(Casuals)

# admin.site.register(Ethnics)

# admin.site.register(Parties)

# admin.site.register(Birthdays)

# admin.site.register(Mom_daughters)

# admin .site.register(cart , cartItem)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product, Gown, Accessories, Birthdays, Casuals, Ethnics, MomDaughters, Parties, Cart, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Gown)
admin.site.register(Accessories)
admin.site.register(Birthdays)
admin.site.register(Casuals)
admin.site.register(Ethnics)
admin.site.register(MomDaughters)
admin.site.register(Parties)
admin.site.register(Cart)
admin.site.register(CartItem)

# Unregister the built-in User model and register it with the custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





