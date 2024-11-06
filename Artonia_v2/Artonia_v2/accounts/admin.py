from django.contrib import admin

from Artonia_v2.accounts.models import ArtoniaUser


@admin.register(ArtoniaUser)
class UserRegisterViewAdmin(admin.ModelAdmin):
    pass
