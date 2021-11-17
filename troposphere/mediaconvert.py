# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.1.0


from . import AWSObject, AWSProperty
from .validators import integer


class AccelerationSettings(AWSProperty):
    props = {
        "Mode": (str, True),
    }


class JobTemplate(AWSObject):
    resource_type = "AWS::MediaConvert::JobTemplate"

    props = {
        "AccelerationSettings": (AccelerationSettings, False),
        "Category": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "Priority": (integer, False),
        "Queue": (str, False),
        "SettingsJson": (dict, True),
        "StatusUpdateInterval": (str, False),
        "Tags": (dict, False),
    }


class Preset(AWSObject):
    resource_type = "AWS::MediaConvert::Preset"

    props = {
        "Category": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "SettingsJson": (dict, True),
        "Tags": (dict, False),
    }


class Queue(AWSObject):
    resource_type = "AWS::MediaConvert::Queue"

    props = {
        "Description": (str, False),
        "Name": (str, False),
        "PricingPlan": (str, False),
        "Status": (str, False),
        "Tags": (dict, False),
    }
