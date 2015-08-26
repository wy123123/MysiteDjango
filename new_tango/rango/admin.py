from django.contrib import admin
from .models import Regions,Shippers,Suppliers,Category,Page

class PageAdmin(admin.ModelAdmin):

    list_display = ('title','category','url')

admin.site.register(Regions)
admin.site.register(Shippers)
admin.site.register(Suppliers)
admin.site.register(Category)
admin.site.register(Page,PageAdmin)