from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, FileResponse
from django.template import loader

from app.settings import BASE_DIR
from .models import Apk, InformationMessage

# Create your views here.

def index(request):
    apk = get_object_or_404(
        Apk.objects.order_by('-added_at')[:1],
    )
    message = InformationMessage.objects.get(pk=1)
    context = {
        'message': message,
        'apk': apk
    }

    return render(request, 'apk/index.html', context)