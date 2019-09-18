# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TokenModel(Model):
    """Token.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    """

    _validation = {
        'model_type': {'readonly': True},
    }

    _attribute_map = {
        'access_token': {'key': 'access_token', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super(TokenModel, self).__init__(**kwargs)
        self.access_token = kwargs.get('access_token', None)
