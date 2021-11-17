# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from . import AWSObject, AWSProperty
from .validators import double


class AnomalyMonitor(AWSObject):
    resource_type = "AWS::CE::AnomalyMonitor"

    props = {
        "MonitorDimension": (str, False),
        "MonitorName": (str, True),
        "MonitorSpecification": (str, False),
        "MonitorType": (str, True),
    }


class Subscriber(AWSProperty):
    props = {
        "Address": (str, True),
        "Status": (str, False),
        "Type": (str, True),
    }


class AnomalySubscription(AWSObject):
    resource_type = "AWS::CE::AnomalySubscription"

    props = {
        "Frequency": (str, True),
        "MonitorArnList": ([str], True),
        "Subscribers": ([Subscriber], True),
        "SubscriptionName": (str, True),
        "Threshold": (double, True),
    }


class CostCategory(AWSObject):
    resource_type = "AWS::CE::CostCategory"

    props = {
        "Name": (str, True),
        "RuleVersion": (str, True),
        "Rules": (str, True),
    }