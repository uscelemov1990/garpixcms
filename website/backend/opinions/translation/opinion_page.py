from modeltranslation.translator import TranslationOptions, register
from ..models import OpinionPage


@register(OpinionPage)
class OpinionPageTranslationOptions(TranslationOptions):
    pass
