from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at')
    list_filter = ('book', 'user', 'created_at')
    fields = [('book', 'user'), ('end_at', 'plated_end_at')]

    class Meta:
        model = Order
        model.__str__ = lambda x: f'{x.id} {x.user} {x.book}'


admin.site.register(Order, OrderAdmin)
