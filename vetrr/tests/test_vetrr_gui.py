from __future__ import print_function, absolute_import, division, unicode_literals

# TEST_UNICODE_LITERALS

import pytest
import numpy as np
import os
from pkg_resources import resource_filename


def data_path(filename):
    data_dir = resource_filename('vetrr', 'vetrr/tests/')
    return os.path.join(data_dir, filename)
