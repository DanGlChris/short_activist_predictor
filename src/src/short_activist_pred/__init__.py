# ---------------------------------------------------------------
# Project Name: short-activist-report
# Created by: Daglox Kankwanda
# Username: DanGlChris
# Creation Date: October 21, 2023
#
# Copyright: All rights reserved
# ---------------------------------------------------------------

import sys


if sys.version_info[:2] >= (3, 10):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.10`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "short-activists-pred"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "1.0.1"
finally:
    del version, PackageNotFoundError
