import rest_framework.routers


class DefaultRouter(rest_framework.routers.DefaultRouter):
    """ Improvement of rest_framework.routers.DefaultRouter that allows the
    lookup of urls of nested resources.
    """
    def get_lookup_regex(self, viewset, lookup_prefix=''):
        """
        Given a viewset, return the portion of URL regex that is used
        to match against a single instance.
        """
        base_regex = '(?P<{lookup_prefix}{lookup_field}>[^/]+)'
        lookup_field = getattr(viewset, 'lookup_field', 'pk')
        return base_regex.format(lookup_field=lookup_field, lookup_prefix=lookup_prefix)