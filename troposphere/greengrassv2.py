# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ComponentPlatform(AWSProperty):
    props = {
        "Attributes": (dict, False),
        "Name": (str, False),
    }


class LambdaEventSource(AWSProperty):
    props = {
        "Topic": (str, False),
        "Type": (str, False),
    }


class LambdaDeviceMount(AWSProperty):
    props = {
        "AddGroupOwner": (boolean, False),
        "Path": (str, False),
        "Permission": (str, False),
    }


class LambdaVolumeMount(AWSProperty):
    props = {
        "AddGroupOwner": (boolean, False),
        "DestinationPath": (str, False),
        "Permission": (str, False),
        "SourcePath": (str, False),
    }


class LambdaContainerParams(AWSProperty):
    props = {
        "Devices": ([LambdaDeviceMount], False),
        "MemorySizeInKB": (integer, False),
        "MountROSysfs": (boolean, False),
        "Volumes": ([LambdaVolumeMount], False),
    }


class LambdaLinuxProcessParams(AWSProperty):
    props = {
        "ContainerParams": (LambdaContainerParams, False),
        "IsolationMode": (str, False),
    }


class LambdaExecutionParameters(AWSProperty):
    props = {
        "EnvironmentVariables": (dict, False),
        "EventSources": ([LambdaEventSource], False),
        "ExecArgs": ([str], False),
        "InputPayloadEncodingType": (str, False),
        "LinuxProcessParams": (LambdaLinuxProcessParams, False),
        "MaxIdleTimeInSeconds": (integer, False),
        "MaxInstancesCount": (integer, False),
        "MaxQueueSize": (integer, False),
        "Pinned": (boolean, False),
        "StatusTimeoutInSeconds": (integer, False),
        "TimeoutInSeconds": (integer, False),
    }


class LambdaFunctionRecipeSource(AWSProperty):
    props = {
        "ComponentDependencies": (dict, False),
        "ComponentLambdaParameters": (LambdaExecutionParameters, False),
        "ComponentName": (str, False),
        "ComponentPlatforms": ([ComponentPlatform], False),
        "ComponentVersion": (str, False),
        "LambdaArn": (str, False),
    }


class ComponentVersion(AWSObject):
    resource_type = "AWS::GreengrassV2::ComponentVersion"

    props = {
        "InlineRecipe": (str, False),
        "LambdaFunction": (LambdaFunctionRecipeSource, False),
        "Tags": (Tags, False),
    }
