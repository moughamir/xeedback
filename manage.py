#!seed/bin/python
import os
import sys

from feedapp.boot import fix_path
fix_path()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedapp.settings")

    from djangae.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
