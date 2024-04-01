from django.db import models


class ApkType(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.pk}, label: {self.label}'

class Apk(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    type = models.ForeignKey(ApkType, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    android_apk_url = models.CharField(max_length=255, null=True, blank=True)
    ios_apk_url = models.CharField(max_length=255, null=True, blank=True)
    android_apk_file = models.FileField(upload_to='static/android_apk_file', null=True, blank=True)
    ios_apk_file = models.FileField(upload_to='static/ios_apk_file', null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, version: {self.version}, type: {self.type.label}, added_at: {self.added_at}'


class MessageType(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.pk}, label: {self.label}'

class InformationMessage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.ForeignKey(MessageType, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'id: {self.pk}, title: {self.title}, type: {self.type.label}'