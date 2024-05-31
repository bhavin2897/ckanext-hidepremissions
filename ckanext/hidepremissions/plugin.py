import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from collections import OrderedDict


class HidepremissionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)

    # plugins.implements(plugins.IAuthFunctions,inherit = True)

    def _facets(self, facets_dict, package_type):
        if 'groups' in facets_dict:
            del facets_dict['groups']
            del facets_dict['tags']

            if package_type == 'molecule_view':
                facets_dict = {'organization': 'Repositories',
                               'measurement_technique': 'Measurement Technique',
                               'license_id': 'License'}
            else:
                facets_dict = {'organization': 'Repositories',
                               'measurement_technique': 'Measurement Technique',
                               'license_id': 'License'}

        return facets_dict

    def dataset_facets(self, facets_dict, package_type):
        return self._facets(facets_dict, package_type)

    def group_facets(self, facets_dict, group_type, package_type):
        return self._facets(facets_dict,package_type)

    def organization_facets(self, facets_dict, organization_type,
                            package_type):
        return self._facets(facets_dict,package_type)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'hidepremissions')
