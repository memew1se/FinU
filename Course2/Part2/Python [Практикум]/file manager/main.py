import os
from dotenv import load_dotenv
from pyshell import shell
from commands import PYSHELL_COMMANDS


if __name__ == '__main__':
    PH = '/'

    if os.name == "posix" or os.name == "mac":
        PH = os.getenv('HOME') + '/tmp'

    elif os.name == 'nt':
        PH = os.environ.get('HOMEPATH') + r'\tmp'

    with open('.env', 'w') as file:
        file.write(f'PYSHELL_HOME={PH}')

    load_dotenv()
    HOME_PATH = os.getenv('PYSHELL_HOME')
    os.chdir(HOME_PATH)
    shell()
