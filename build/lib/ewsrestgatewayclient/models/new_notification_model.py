# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NewNotificationModel(Model):
    """Describes how a Notification will be created for a give Subscription.

    :param subscription_id: Id of the Subscription the Notification will be
     created under.
    :type subscription_id: str
    :param changes_only: If true, all items will be returned.  If false, only
     changes since the last Notification for the Subscription will be created.
    :type changes_only: bool
    """

    _attribute_map = {
        'subscription_id': {'key': 'SubscriptionId', 'type': 'str'},
        'changes_only': {'key': 'ChangesOnly', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(NewNotificationModel, self).__init__(**kwargs)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.changes_only = kwargs.get('changes_only', None)
