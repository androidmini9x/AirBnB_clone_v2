#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from time import strftime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    filename = strftime("%Y%m%d%H%M%S")
    output = "versions/web_static_{}.tgz".format(filename)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output
