# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SystemEventTypeModel(Model):
    """Defines a "Type" for an SystemEvent.

    :param name: Name of the entity.
    :type name: str
    :param description: Optional description of the SystemEventType.
    :type description: str
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, description: str=None, id: str=None, **kwargs) -> None:
        super(SystemEventTypeModel, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.id = id
