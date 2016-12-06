from fabric.api import *
import fabric.contrib.project as project
import os

env.use_ssh_config = True

DEPLOY_PATH = 'output'
env.deploy_path = DEPLOY_PATH

# Remote server configuration
production = 'venus'
dest_path = '/var/www/geophysics/www/ROMY/'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican content -d -s pelicanconf.py -o output')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican content -d -r -s pelicanconf.py -o output')

def serve():
    build()
# SD Dec 2016
#    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))
    local('cd {deploy_path} && python -m http.server'.format(**env))

@hosts(production)
def publish():
    local('pelican content -d -s pelicanconf.py -o output')
    local('rm -rf output/theme/.svn')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=[".DS_Store", "images/large_files"],
        local_dir=DEPLOY_PATH.rstrip('/') + '/*',
        delete=True,
        extra_opts="--omit-dir-times --chmod=Dug=rwx,Do=rx,Fug=rw,Fo=r"
    )
