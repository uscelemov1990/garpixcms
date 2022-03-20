from mysettings.models import MySetting
from garpix_menu.utils import get_menus

from mysettings.serializers import MySettingSerializer


def global_context(request, page):
    menus = get_menus(page.get_absolute_url())
    my_setting = MySetting.get_solo()

    return {
        'menus': menus,
        'mysetting': MySettingSerializer(my_setting).data,
    }
