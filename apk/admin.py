from django.contrib import admin

from .models import ApkType, Apk, MessageType, InformationMessage

admin.site.register(ApkType)
admin.site.register(Apk)
admin.site.register(MessageType)
admin.site.register(InformationMessage)
