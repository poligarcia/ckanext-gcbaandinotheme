from ckan.lib import base
import logging

logger = logging.getLogger(__name__)


class GcbaAndinoThemeController(base.BaseController):

    def historias(self):
        return base.render('historias.html')
