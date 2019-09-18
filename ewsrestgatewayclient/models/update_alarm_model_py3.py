# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateAlarmModel(Model):
    """Describes how an Alarm will be patched.

    :param name: Name of the Alarm.
    :type name: str
    :param description: Optional description of the Alarm.
    :type description: str
    :param parent_id: Id of the Container which the Alarm is found in.
    :type parent_id: str
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'parent_id': {'key': 'ParentId', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, description: str=None, parent_id: str=None, id: str=None, **kwargs) -> None:
        super(UpdateAlarmModel, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.id = id