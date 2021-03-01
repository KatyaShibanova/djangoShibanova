from django.contrib import admin

from .models import Deals, Dogs, Characters


class DogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'dogName', 'description', 'weight', 'height', 'age', 'price')
    list_display_links = ('id', 'dogName', 'description')
    search_fields = ('dogName', 'description',)


class DealsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'dogs', 'additionalInfo', 'date')
    list_display_links = ('id', 'client', 'dogs')
    search_fields = ('additionalInfo', )


admin.site.register(Deals, DealsAdmin)
admin.site.register(Characters)
admin.site.register(Dogs, DogsAdmin)