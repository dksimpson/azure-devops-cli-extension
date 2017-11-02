# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import dateutil.parser
import dateutil.tz

from collections import OrderedDict
from vsts.cli.team.common.project import (PROCESS_TEMPLATE_CAPABILITY_NAME,
                                          PROCESS_TEMPLATE_CAPABILITY_TEMPLATE_TYPE_ID_ATTRIBUTE_NAME,
                                          VERSION_CONTROL_CAPABILITY_NAME,
                                          VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME)


def transform_project_table_output(result):
    table_output = [_transform_project_row(result)]
    return table_output


def _transform_project_row(row):
    table_row = OrderedDict()
    table_row['ID'] = row['id']
    table_row['Name'] = row['name']
    table_row['State'] = row['state']

    if 'capabilities' in row:
        capabilities = row['capabilities']
        if PROCESS_TEMPLATE_CAPABILITY_NAME in capabilities:
            process_capabilities = capabilities[PROCESS_TEMPLATE_CAPABILITY_NAME]
            if 'templateName' in process_capabilities:
                table_row['Template'] = process_capabilities['templateName']
        if VERSION_CONTROL_CAPABILITY_NAME in capabilities:
            version_capabilities = capabilities[VERSION_CONTROL_CAPABILITY_NAME]
            if VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME in version_capabilities:
                table_row['Source Control'] = version_capabilities[VERSION_CONTROL_CAPABILITY_ATTRIBUTE_NAME]

    return table_row
