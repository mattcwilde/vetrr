from __future__ import print_function, absolute_import, division, unicode_literals

# TEST_UNICODE_LITERALS

import pytest
import os
from pkg_resources import resource_filename

from linetools.guis import xspecgui

# Set of Input lines
def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), '../files')
    return os.path.join(data_dir, filename)

def test_xspecgui():
    # Init
    spec_fil = data_path('J105935.22+144406.3.fits.gz')
    xsgui = xspecgui.XSpecGui(spec_fil, unit_test=True)
