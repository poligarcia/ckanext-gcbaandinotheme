import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class GcbaAndinoThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.interfaces.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'gcbaandinotheme')

    def before_map(self, m):
        return m

    def after_map(self, m):
        m.connect('historias', "/historias-con-datos",
                  controller='ckanext.gcbaandinotheme.plugin_controller:GcbaAndinoThemeController',
                  action='historias')
        return m
