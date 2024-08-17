# my_python_module/__init__.py

"""
Matilde
================

Perform website audits
"""

__version__ = "0.1.0"

from .main import run_audits


__all__ = [
    "run_audits",
]
