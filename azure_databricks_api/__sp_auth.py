import requests


class ServicePrincipalAuth(object):

    def __init__(self, **kwargs):
        self._tenant_id = kwargs.pop('tenant_id')
        self._client_id = kwargs.pop('client_id')
        self._client_secret = kwargs.pop('client_secret')
        self._databricks_resource_id = kwargs.pop('databricks_resource_id')

    def authenticate(self):
        auth_headers = {'Content-Type': "application/x-www-form-urlencoded"}
        application_id = '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d'
        aad_authentication_endpoint = 'https://login.microsoftonline.com/{}/oauth2/token'.format(self._tenant_id)
        management_resource_endpoint = "https://management.core.windows.net/"

        azure_ad_auth_data = {'grant_type': 'client_credentials', 'client_id': self._client_id,
                              'resource': application_id, 'client_secret': self._client_secret}
        azure_ad_auth_response = requests.post(aad_authentication_endpoint, headers=auth_headers,
                                               data=azure_ad_auth_data)
        arm_token = azure_ad_auth_response.json()['access_token']

        management_endpoint_auth_data = {'grant_type': 'client_credentials', 'client_id': self._client_id,
                                         'resource': management_resource_endpoint, 'client_secret': self._client_secret}
        management_endpoint_auth_response = requests.post(aad_authentication_endpoint, headers=auth_headers,
                                                          data=management_endpoint_auth_data)
        adb_token = management_endpoint_auth_response.json()['access_token']

        headers = {'Authorization': 'Bearer {0}'.format(arm_token),
                   'X-Databricks-Azure-SP-Management-Token': adb_token,
                   'X-Databricks-Azure-Workspace-Resource-Id': self._databricks_resource_id
                   }

        return headers
