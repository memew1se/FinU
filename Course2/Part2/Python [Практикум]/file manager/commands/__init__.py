from .cat import Cat
from .cd import Cd
from .copy import Copy
from .echo import Echo
from .ls import Ls
from .man import Man
from .mkdir import Mkdir
from .move import Move
from .rename import Rename
from .rm import Rm
from .touch import Touch

cd.Cd()

PYSHELL_COMMANDS = {'cat': Cat,
                    'cd': Cd,
                    'copy': Copy,
                    'echo': Echo,
                    'ls': Ls,
                    'man': Man,
                    'mkdir': Mkdir,
                    'move': Move,
                    'rename': Rename,
                    'rm': Rm,
                    'touch': Touch
                    }

Man.setCommands(PYSHELL_COMMANDS)

__all__ = ['PYSHELL_COMMANDS']
