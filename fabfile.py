from fabric.api import *
import fabric.contrib.project as project
import os

env.use_ssh_config = True

DEPLOY_PATH = 'output'
env.deploy_path = DEPLOY_PATH

# Remote server configuration
production = 'venus'
dest_path = '/var/www/geophysics/www/ROMY'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican content -s pelicanconf.py -o output')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican content -r -s pelicanconf.py -o output')

def serve():
    build()
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

@hosts(production)
def publish():
    local('pelican content -s pelicanconf.py -o output')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts="--no-perms --omit-dir-times"
    )
