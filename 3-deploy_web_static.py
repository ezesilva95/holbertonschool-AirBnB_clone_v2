#!/usr/bin/python3
"""
"""

from fabric.api import local, env, put, run
from time import strftime
import os.path
env.hosts = ['54.163.195.60', '3.87.124.19']


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploy archive to web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except Exception:
        return False


def deploy():
    """
    all the do_pack() function and store the path of the created archive
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
