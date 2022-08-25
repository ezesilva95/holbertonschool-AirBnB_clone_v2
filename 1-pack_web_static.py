#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has been
correctly generated. Otherwise, it should return None
"""

from fabric.api import local
from time import strftime


def do_pack():
    """
    """
    time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None
