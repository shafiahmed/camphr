"""
This type stub file was generated by pyright.
"""

import warnings
import sys
from __future__ import unicode_literals
from thinc.neural.util import prefer_gpu, require_gpu
from . import pipeline, util
from .cli.info import info as cli_info
from .glossary import explain
from .about import __version__
from .errors import Errors, Warnings, deprecation_warning
from .util import registry
from .language import Language, component
from typing import Any, Optional

if sys.maxunicode == 65535: ...

def load(name, **overrides) -> Language: ...
def blank(name, **kwargs) -> Language: ...
def info(model: Optional[Any] = ..., markdown: bool = ..., silent: bool = ...): ...

__all__ = ["load", "blank", "info", "component"]

