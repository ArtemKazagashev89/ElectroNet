from django.contrib import admin
from .models import Factory, RetailNetwork, IndividualEntrepreneur


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'debt_to_supplier', 'created_at')
    list_filter = ('city',)  # Фильтр по названию города
    search_fields = ('name', 'city')  # Поиск по имени и городу


class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'debt_to_supplier', 'created_at', 'supplier_link')
    list_filter = ('city',)  # Фильтр по названию города
    search_fields = ('name', 'city')  # Поиск по имени и городу
    actions = ['clear_debt']  # Доступные действия

    def supplier_link(self, obj):
        return obj.supplier.name if obj.supplier else "Нет поставщика"
    supplier_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt_to_supplier = 0.00
            obj.save()
        self.message_user(request, "Задолженность успешно очищена.")
    clear_debt.short_description = "Очистить задолженность у выбранных объектов"


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'debt_to_supplier', 'created_at', 'supplier_link')
    list_filter = ('city',)  # Фильтр по названию города
    search_fields = ('name', 'city')  # Поиск по имени и городу

    def supplier_link(self, obj):
        return obj.supplier.name if obj.supplier else "Нет поставщика"
    supplier_link.short_description = "Поставщик"


admin.site.register(Factory, FactoryAdmin)
admin.site.register(RetailNetwork, RetailNetworkAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)