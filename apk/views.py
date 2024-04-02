import os

import environ
import base64

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, FileResponse
from django.template import loader
from app.settings import BASE_DIR
from .models import Apk, InformationMessage

env = environ.Env()
_DEV_MAIL = env('DEV_MAIL', default='maengdok@outlook.com')

def index(request):
    apk = get_object_or_404(
        Apk.objects.order_by('-added_at')[:1],
    )
    message = InformationMessage.objects.get(pk=1)
    context = {
        'message': message,
        'apk': apk,
        'dev_mail': base64.b64encode(bytes(_DEV_MAIL, 'utf-8'))
    }

    return render(request, 'apk/index.html', context)