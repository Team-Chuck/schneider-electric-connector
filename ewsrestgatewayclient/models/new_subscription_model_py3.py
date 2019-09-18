# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NewSubscriptionModel(Model):
    """Represents a Subscription creation request.

    :param duration_in_minutes: The requested  duration of the Subscription.
    :type duration_in_minutes: int
    :param subscription_type: The type of data to Subscribe to. Possible
     values include: 'ValueItemChanged', 'AlarmEventChanged',
     'SystemEventChanged', 'HierarchyChanged'
    :type subscription_type: str or ~ewsrestgatewayswagger.models.enum
    :param ids: List of Ids of items which are being Subscribed to.
    :type ids: list[str]
    :param priority_from: For AlarmEventChanged and SystemEventChanged
     subscriptions, only items with Priority at or above this value will be
     included.
    :type priority_from: int
    :param priority_to: For AlarmEventChanged and SystemEventChanged
     subscriptions, only items with Priority below this value will be included.
    :type priority_to: int
    :param types: For AlarmEventChanged and SystemEventChanged subscriptions,
     only items with a Type in this List will be included.
    :type types: list[str]
    """

    _attribute_map = {
        'duration_in_minutes': {'key': 'DurationInMinutes', 'type': 'int'},
        'subscription_type': {'key': 'SubscriptionType', 'type': 'str'},
        'ids': {'key': 'Ids', 'type': '[str]'},
        'priority_from': {'key': 'PriorityFrom', 'type': 'int'},
        'priority_to': {'key': 'PriorityTo', 'type': 'int'},
        'types': {'key': 'Types', 'type': '[str]'},
    }

    def __init__(self, *, duration_in_minutes: int=None, subscription_type=None, ids=None, priority_from: int=None, priority_to: int=None, types=None, **kwargs) -> None:
        super(NewSubscriptionModel, self).__init__(**kwargs)
        self.duration_in_minutes = duration_in_minutes
        self.subscription_type = subscription_type
        self.ids = ids
        self.priority_from = priority_from
        self.priority_to = priority_to
        self.types = types
