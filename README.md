# Azure Databricks API Wrapper
A Python, object-oriented wrapper for the [Azure Databricks REST API 2.0](https://docs.azuredatabricks.net/api/latest/index.html)

### Installation
This package is pip installable.
```bash
pip install azure-databricks-api
```

### Implemented APIs
As of October 17th, 2019 there are 10 different services available in the Azure Databricks API. Currently, the following services are supported by the Azure Databricks API Wrapper.
* [x] Clusters
* [x] Groups
* [x] Token
* [x] Workspace
* [x] DBFS
* [X] Libraries
* [ ] Jobs
* [ ] Instance Pools
* [ ] Secrets
* [ ] SCIM _(Preview)_


### Client Instantiation For Use With Personal Access Tokens
To create the client object, you pass the Azure region your workspace is located in and the [generated Personal Access Token](https://docs.databricks.com/api/latest/authentication.html#generate-a-token)
```python
from azure_databricks_api import AzureDatabricksRESTClient
from azure_databricks_api import PersonalAccessTokenAuth

azure_region = '[INSERT YOUR REGION]'
token = '[INSERT YOUR PERSONAL ACCESS TOKEN]' 

client = AzureDatabricksRESTClient(region=azure_region, token=token)
```

### Client Instantiation For Use With Service Principal
```python
from azure_databricks_api import AzureDatabricksRESTClient
from azure_databricks_api import ServicePrincipalAuth

azure_region = '[INSERT YOUR REGION]'
tenant_id = '[INSERT YOUR AZURE TENANT ID]'
client_id = '[INSERT YOUR AZURE AD APPLICATION CLIENT ID]'
client_secret = '[INSERT YOUR AZURE AD APPLICATION CLIENT SECRET]'
databricks_resource_id = '[INSERT THE RESOURCE ID OF YOUR DATABRICKS WORKSPACE]'

credentials = ServicePrincipalAuth(tenant_id = tenant_id, client_id = client_id, client_secret = client_secret,
                                   databricks_resource_id = databricks_resource_id)

client = AzureDatabricksRESTClient(azure_region, credentials)
```
### Clusters Client Usage
The services above are implements as children objects of the client. For example, to pin a cluster, you can either pass the cluster_name or cluster_id:
```python
client.clusters.pin('test_cluster_name')
```

The other services are implemented similarly. (e.g. `client.tokens` or `client.groups`) 

