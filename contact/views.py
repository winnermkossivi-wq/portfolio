import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Message

logger = logging.getLogger(__name__)


def contact(request):
    if request.method == 'POST':
        message = Message.objects.create(
            nom=request.POST.get('nom', ''),
            email=request.POST.get('email', ''),
            sujet=request.POST.get('sujet', ''),
            contenu=request.POST.get('contenu', ''),
        )
        try:
            send_mail(
                subject=f"[Portfolio] {message.sujet or 'Nouveau message'}",
                message=(
                    f"Nom : {message.nom}\n"
                    f"Email : {message.email}\n"
                    f"Sujet : {message.sujet}\n\n"
                    f"{message.contenu}\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT],
                fail_silently=False,
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("Échec de l'envoi d'email depuis le contact : %s", exc)
        messages.success(request, "Votre message a bien été envoyé.")
        return redirect('contact:contact')
    return render(request, 'contact/contact.html')