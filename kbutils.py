import atexit
import os
if os.name == 'nt':
    import msvcrt
else:
    import sys
    import termios


old_settings=None


if os.name != 'nt':
    old_settings = termios.tcgetattr(sys.stdin)
    new_settings = termios.tcgetattr(sys.stdin)
    new_settings[3] = new_settings[3] & ~(termios.ECHO | termios.ICANON) # lflags
    new_settings[6][termios.VMIN] = 0  # cc
    new_settings[6][termios.VTIME] = 0 # cc
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

    @atexit.register
    def term_anykey():
        global old_settings
        if old_settings:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def get_char():
    # figure out which function to use once, and store it in _func
    if os.name == 'nt':
        if msvcrt.kbhit():
            return msvcrt.getch()
        else:
            return None
    else:
        v = os.read(sys.stdin.fileno(), 1)
        if v and len(v) > 0:
            return v.decode('latin1')
        else:
            return v
