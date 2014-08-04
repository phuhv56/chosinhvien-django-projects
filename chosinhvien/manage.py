#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chosinhvien.settings")

    from django.core.management import execute_from_command_line

    a = []
    a.append("manage.py")
    a.append("runserver")
    #execute_from_command_line(sys.argv)

    execute_from_command_line(a)
