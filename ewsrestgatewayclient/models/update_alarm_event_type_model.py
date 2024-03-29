# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateAlarmEventTypeModel(Model):
    """Describes how a Trend will be patched.

    :param name: Name of the entity.
    :type name: str
    :param description: Optional description of the AlarmEventType.
    :type description: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpdateAlarmEventTypeModel, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
