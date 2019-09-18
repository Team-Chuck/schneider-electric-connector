# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateContainerModel(Model):
    """Describes how a Container will be patched.

    :param name: Name of the Container.
    :type name: str
    :param description: Optional description of the Container.
    :type description: str
    :param type: Specifies the type of the Container. Possible values include:
     'Folder', 'Server', 'Device', 'Structure', 'Service'
    :type type: str or ~ewsrestgatewayswagger.models.enum
    :param parent_id: Id of the Container which the Container is found in.
    :type parent_id: str
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'type': {'key': 'Type', 'type': 'str'},
        'parent_id': {'key': 'ParentId', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, description: str=None, type=None, parent_id: str=None, id: str=None, **kwargs) -> None:
        super(UpdateContainerModel, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.type = type
        self.parent_id = parent_id
        self.id = id