import os
import sys
import subprocess

def find_vboxmanage():

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    paths = os.environ["PATH"].split(os.pathsep)

    if sys.platform == 'win32':
        # Add the standard install location
        paths.append('C:\\Program Files\\Oracle\\VirtualBox')
        program = 'VBoxManage.exe'
    else:
        program = 'vboxmanage'

    for path in paths:
        exe_file = os.path.join(path, program)
        if is_exe(exe_file):
            return exe_file

    return None

vboxmanage = find_vboxmanage()
print("Location:", vboxmanage)

_system_properties = None

def system_properties():
    global _system_properties
    if _system_properties is None:
        print("Getting system properties")
        out = subprocess.check_output(
                [vboxmanage, 'list', 'systemproperties'],
                universal_newlines=True)
        _system_properties = {}
        for line in out.splitlines():
            k, v = line.split(':', 1)
            _system_properties[k.strip()] = v.strip()
    return _system_properties
