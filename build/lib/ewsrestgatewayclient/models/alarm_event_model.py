# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AlarmEventModel(Model):
    """An AlarmEvent represents the transition of an Alarm through the state
    transition model implemented.
    Every transition for an Alarm, including a return to normal generates an
    AlarmEvent instance.

    :param alarm_id: Optional Id of the associated Alarm.
    :type alarm_id: str
    :param acknowledgeable: Acknowledge restrictions of the AlarmEvent.
     Possible values include: 'No', 'Yes', 'Required'
    :type acknowledgeable: str or ~ewsrestgatewayswagger.models.enum
    :param occurred_on: DateTime in UTC when the Alarm most recently
     transitioned into and “alarmed” state - that is not in the "Normal" state.
    :type occurred_on: datetime
    :param last_transitioned_on: DateTime oin UTC when the transition captured
     by this AlarmEvent occurred.
    :type last_transitioned_on: datetime
    :param message: Human readable message for the AlarmEvent.
    :type message: str
    :param priority: Priority value of the AlarmEvent.
    :type priority: int
    :param state: State this AlarmEvent transition is documenting. Possible
     values include: 'Normal', 'Active', 'Acknowledged', 'Reset', 'Disabled'
    :type state: str or ~ewsrestgatewayswagger.models.enum
    :param type: Server specific type of the AlarmEvent.
    :type type: str
    :param alarm_source_name: The name of the source of the alarm event.
    :type alarm_source_name: str
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'alarm_id': {'key': 'AlarmId', 'type': 'str'},
        'acknowledgeable': {'key': 'Acknowledgeable', 'type': 'str'},
        'occurred_on': {'key': 'OccurredOn', 'type': 'iso-8601'},
        'last_transitioned_on': {'key': 'LastTransitionedOn', 'type': 'iso-8601'},
        'message': {'key': 'Message', 'type': 'str'},
        'priority': {'key': 'Priority', 'type': 'int'},
        'state': {'key': 'State', 'type': 'str'},
        'type': {'key': 'Type', 'type': 'str'},
        'alarm_source_name': {'key': 'AlarmSourceName', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AlarmEventModel, self).__init__(**kwargs)
        self.alarm_id = kwargs.get('alarm_id', None)
        self.acknowledgeable = kwargs.get('acknowledgeable', None)
        self.occurred_on = kwargs.get('occurred_on', None)
        self.last_transitioned_on = kwargs.get('last_transitioned_on', None)
        self.message = kwargs.get('message', None)
        self.priority = kwargs.get('priority', None)
        self.state = kwargs.get('state', None)
        self.type = kwargs.get('type', None)
        self.alarm_source_name = kwargs.get('alarm_source_name', None)
        self.id = kwargs.get('id', None)
