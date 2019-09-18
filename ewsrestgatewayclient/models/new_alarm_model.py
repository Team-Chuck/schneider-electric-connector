# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NewAlarmModel(Model):
    """Describes how an Alarm will be created.

    :param value_id: Optional Id of a Value this Alarm is associated with.
    :type value_id: str
    :param transition_model: The transition model for the Alarm. Possible
     values include: 'Unrestricted', 'SimpleSystemAlarm',
     'NoAcknowledgeRequired', 'SimpleTransientAlarm',
     'SingleAcknowledgeRequirement', 'ExtendedAcknowledgeRequirement'
    :type transition_model: str or ~ewsrestgatewayswagger.models.enum
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
        'value_id': {'key': 'ValueId', 'type': 'str'},
        'transition_model': {'key': 'TransitionModel', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'parent_id': {'key': 'ParentId', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NewAlarmModel, self).__init__(**kwargs)
        self.value_id = kwargs.get('value_id', None)
        self.transition_model = kwargs.get('transition_model', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.parent_id = kwargs.get('parent_id', None)
        self.id = kwargs.get('id', None)
