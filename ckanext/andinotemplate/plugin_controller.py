from ckan.lib import base
import logging

logger = logging.getLogger(__name__)


class GcbaAndinoThemeController(base.BaseController):

    def seccion_nueva(self):
        return base.render('template_nuevo.html')  # Especificamos el template
