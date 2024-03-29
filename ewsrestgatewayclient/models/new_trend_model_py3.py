# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NewTrendModel(Model):
    """Describes how an Container will be created.

    :param value_id: Id of the Value for which trending data will be captured.
    :type value_id: str
    :param name: Name of the Trend.
    :type name: str
    :param description: Optional description of the Trend.
    :type description: str
    :param parent_id: Id of the Container which the Trend is found in.
    :type parent_id: str
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'value_id': {'key': 'ValueId', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'parent_id': {'key': 'ParentId', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, *, value_id: str=None, name: str=None, description: str=None, parent_id: str=None, id: str=None, **kwargs) -> None:
        super(NewTrendModel, self).__init__(**kwargs)
        self.value_id = value_id
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.id = id
