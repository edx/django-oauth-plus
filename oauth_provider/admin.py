from __future__ import absolute_import

from django.contrib import admin

from .models import Consumer, Scope, Token


class ScopeAdmin(admin.ModelAdmin):
    pass


class ConsumerAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']


class TokenAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'consumer', 'scope']


admin.site.register(Scope, ScopeAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Token, TokenAdmin)
