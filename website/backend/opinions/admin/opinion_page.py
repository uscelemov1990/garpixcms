from ..models.opinion_page import OpinionPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OpinionPage)
class OpinionPageAdmin(BasePageAdmin):
    pass
