# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NotificationModel(Model):
    """A Notification represents a logical session of NotificationItem for a
    Subscription at point in time.

    :param subscription_id: The Subscription that this Notification is for.
    :type subscription_id: str
    :param created_on: DateTime in UTC when the Notification session was
     created.
    :type created_on: datetime
    :param notification_item_count: The number of available NotificationItems
     for this Notification session
    :type notification_item_count: int
    :param id: Case sensitive identifier for the entity.
    :type id: str
    """

    _attribute_map = {
        'subscription_id': {'key': 'SubscriptionId', 'type': 'str'},
        'created_on': {'key': 'CreatedOn', 'type': 'iso-8601'},
        'notification_item_count': {'key': 'NotificationItemCount', 'type': 'int'},
        'id': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NotificationModel, self).__init__(**kwargs)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.created_on = kwargs.get('created_on', None)
        self.notification_item_count = kwargs.get('notification_item_count', None)
        self.id = kwargs.get('id', None)
