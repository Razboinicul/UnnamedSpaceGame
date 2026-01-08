__version__ = "0.0.3-alpha"
__license__ = "MIT"

import contextlib

with contextlib.redirect_stdout(None):
  import sys
  import pygame as pg
  from .window import *
  from .input import *
  from .etypes import *
  from .entities import *
  from .components import *
  from .assets import *
  from .systems import *
  # from .animated import *
  # from .gui import *
  # from .saving import *
  # from .tiles import *
  # from .scenes import *
  # from .camera import *
  # #0.0.2
  # # from .pkging import *
  # from .states import *

pg.init()

print(
  f"Unamed Space Engine {__version__}",
  f"python {sys.version.split()[0]}  pygame-ce {pg.version.ver}",
  f"© 2025 Unnamed Space Engine Team, GitHub contributors,",
  f"licensed under {__license__}",
  sep="\n",
  end="\n\n"
)
print("*** DEBUG INFORMATION ***")