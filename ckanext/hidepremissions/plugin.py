import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def no_registering(context, data_dict):
    return {
        'success': False,
        'msg': toolkit._(
            'You cannot register.'
        )
    }

class HidepremissionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IAuthFunctions,inherit = True)

    def _facets(self, facets_dict):
        if 'groups' in facets_dict:
            del facets_dict['groups']
        facets_dict['organization'] = toolkit._('Repository')
        return facets_dict

    def dataset_facets(self, facets_dict, package_type):
        return self._facets(facets_dict)

    def group_facets(self, facets_dict, group_type, package_type):
        return self._facets(facets_dict)

    def organization_facets(self, facets_dict, organization_type,
                            package_type):
        return self._facets(facets_dict)

    def get_auth_functions(self):
        return {
            'user_create': no_registering
        }

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'hidepremissions')
