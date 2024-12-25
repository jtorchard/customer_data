# Register your models here.

from django.contrib import admin

from .models import Customer, BankAccount, Licence


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 0


class LicenceInline(admin.StackedInline):
    model = Licence
    extra = 0


class LicenceAdmin(admin.ModelAdmin):
    empty_value_display = "Nadda"
    autocomplete_fields = ["customer"]
    list_display = ["surname", "number", "pub_date", "address", "image"]


class BankAccountAdmin(admin.ModelAdmin):
    empty_value_display = "Nadda"
    autocomplete_fields = ["customer"]
    list_display = ["account_number", "customer__surname", "pub_date"]
    search_fields = ["account_number", "customer__surname", "pub_date"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["surname", "given_names", "licences", "bankaccounts"]
    list_filter = ["pub_date"]
    search_fields = ["surname", "given_names"]
    inlines = [
        BankAccountInline,
        LicenceInline,
    ]

    def licences(self, obj):
        return " || ".join([licence.number for licence in obj.licence_set.all()])

    def bankaccounts(self, obj):
        return " || ".join([bankaccount.account_number for bankaccount in obj.bankaccount_set.all()])

    empty_value_display = "Nadda"


admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Licence, LicenceAdmin)
