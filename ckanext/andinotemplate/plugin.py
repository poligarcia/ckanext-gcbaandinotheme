import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class AndinoTemplatePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.interfaces.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'andinotemplate')

    def before_map(self, m):
        return m

    def after_map(self, m):
        m.connect('seccion-nueva', "/seccion-nueva",
                  controller='ckanext.andinotemplate.plugin_controller:AndinoTemplateController',
                  action='seccion_nueva')
        return m
