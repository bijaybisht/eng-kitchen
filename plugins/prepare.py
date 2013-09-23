"""Installs rsync and chef """

from fabric.api import *

def execute(Node=None):
  run("yum install rsync")
  run("curl -L https://www.opscode.com/chef/install.sh | bash")
