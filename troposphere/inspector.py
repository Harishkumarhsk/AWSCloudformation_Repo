# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .validators import integer


class AssessmentTarget(AWSObject):
    resource_type = "AWS::Inspector::AssessmentTarget"

    props = {
        "AssessmentTargetName": (str, False),
        "ResourceGroupArn": (str, False),
    }


class AssessmentTemplate(AWSObject):
    resource_type = "AWS::Inspector::AssessmentTemplate"

    props = {
        "AssessmentTargetArn": (str, True),
        "AssessmentTemplateName": (str, False),
        "DurationInSeconds": (integer, True),
        "RulesPackageArns": ([str], True),
        "UserAttributesForFindings": (Tags, False),
    }


class ResourceGroup(AWSObject):
    resource_type = "AWS::Inspector::ResourceGroup"

    props = {
        "ResourceGroupTags": (Tags, True),
    }