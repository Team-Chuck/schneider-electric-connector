# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AlarmEventStateChangeInfo(Model):
    """Represents the information needed when manually generating an AlarmEvent
    for an Alarm.

    :param new_state: The new State value for the AlarmEvent. Possible values
     include: 'Normal', 'Active', 'Acknowledged', 'Reset', 'Disabled'
    :type new_state: str or ~ewsrestgatewayswagger.models.enum
    :param new_acknowledgeable: The new Acknowledgeable value for the
     AlarmEvent. Possible values include: 'No', 'Yes', 'Required'
    :type new_acknowledgeable: str or ~ewsrestgatewayswagger.models.enum
    :param message: The Message to be given with the generated AlarmEvent.
    :type message: str
    :param type: The Type of to be given with the generated AlarmEvent.
    :type type: str
    :param priority: The Priority to be given to the genreated AlarmEvent.
    :type priority: int
    """

    _attribute_map = {
        'new_state': {'key': 'NewState', 'type': 'str'},
        'new_acknowledgeable': {'key': 'NewAcknowledgeable', 'type': 'str'},
        'message': {'key': 'Message', 'type': 'str'},
        'type': {'key': 'Type', 'type': 'str'},
        'priority': {'key': 'Priority', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AlarmEventStateChangeInfo, self).__init__(**kwargs)
        self.new_state = kwargs.get('new_state', None)
        self.new_acknowledgeable = kwargs.get('new_acknowledgeable', None)
        self.message = kwargs.get('message', None)
        self.type = kwargs.get('type', None)
        self.priority = kwargs.get('priority', None)
