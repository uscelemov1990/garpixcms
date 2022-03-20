from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.conf import settings
from garpix_page.models import BasePage
from garpix_notify.models import Notify

from ..forms import FeedbackForm
from ..serializers import FeedbackSerializer


class OpinionPage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    postal_address = models.CharField(max_length=250, blank=True, default='', verbose_name='Почтовый адрес')

    template = "pages/opinion.html"

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save()
                Notify.send(settings.FEEDBACK_EVENT, {
                    'feedback': feedback,
                }, email=feedback.email)
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })
            context.update({
                'form': form,
            })

        return context

    class Meta:
        verbose_name = "Opinion"
        verbose_name_plural = "Opinions"
        ordering = ("-created_at",)
