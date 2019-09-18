
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TokenOperations(object):
    """RootOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_token(
            self, username, password, custom_headers=None, raw=False, **operation_config):
        """ Gets new auth token
        """
        # Construct URL
        url = self.get_token.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        #header_parameters['Content-Type'] = 'application/x-www-form-urlencoded'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        #body_content = self._serialize.body("grant_type=password&username=" + username + "&password=" + password, 'str')
        body_content = "grant_type=password&username=" + username + "&password=" + password

        #body_content = {'grant_type':'password', 'username':username, 'password':password}

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        request.data = request.data.strip('"\'')
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TokenModel', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_token.metadata = {'url': '/GetToken'}