# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse

from knack.util import CLIError

# pylint:disable=protected-access, too-few-public-methods

# TODO: update this for the actual model
class FooRuleAddAction(argparse._AppendAction):

    def __call__(self, parser, namespace, values, option_string=None):
        FooRule = namespace._cmd.get_models('FooRule')
        kwargs = {}
        for item in values.split():
            try:
                key, value = item.split('=', 1)
                kwargs[key] = value
            except ValueError:
                raise CLIError('usage error: {} KEY=VALUE [KEY=VALUE ...]'.format(option_string))
        return FooRule(**kwargs)