class PersonalAccessTokenAuth(object):

    def __init__(self, **kwargs):
        self._pat_token = kwargs.pop('pat_token')

    def authenticate(self):
        headers = {'Authorization': 'Bearer {0}'.format(self._pat_token)}
        return headers
