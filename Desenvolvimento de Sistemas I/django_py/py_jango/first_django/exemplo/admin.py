from django.contrib import admin
from exemplo.models import Example
from exemplo.models import Person, Passaport

# Register your models here.

admin.site.register(Example)
admin.site.register(Person)
admin.site.register(Passaport)
