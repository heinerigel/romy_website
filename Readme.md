# Romy Website

## Installing the Dependencies

Python should already be installed on most systems.   
Users of Python 3.x need to install [fabric3](https://pypi.python.org/pypi/Fabric3) and also adjust a lines 33/35 in the file `fabfile.py`.


```bash
# Install pip if not available
$ sudo apt-get install python-pip

# Install pelican
$ pip install pelican
$ pip install markdown

# Install fabric for the deployment
$ pip install fabric
$ pip install fabric3
```


## Getting started

Checkout the git repository

```bash
$ git clone https://github.com/krischer/romy_website.git
$ cd romy_website
```

Inside the svn directory, feel free to edit the files. Most things are written
in [Markdown](http://en.wikipedia.org/wiki/Markdown), a lightweight markup
language or raw HTML. [Pelican](http://docs.getpelican.com/en/3.3.0/) is used
to convert these files to a proper website. Fabric is used to steer that
process, inside the romy directory you have access to the following fabric
commands:

```bash
$ fab build
```

Creates the final HTML filefab buils in the `output/` subdirectory.

```bash
$ fab clean
```

Deletes the `output/` subdirectory.

```bash
$ fab publish
```

Creates the final HTML files in the `output/` subdirectory and copies them to
`venus:/var/www/geophysics/www/ROMY`, essentially publishing them in the web.
Use this when everything works and you want to update the actual website. SSH
has to be configured correctly for this to work (see below).

```bash
$ fab rebuild
```

Executes the `clean` and `build` commands.

```bash
$ fab regenerate
```

Automatically run `build` on every change to a source file.

```bash
$ fab serve
```

Publishes the site on a local [webserver](http://localhost:8000). Best used in
conjunction with `regenerate` when making changes to the website.


## Publishing

If you do not want to correctly configure SSH or have other reasons not to use
fabric, simply copy the contents of the output folder to
`venus:/var/www/geophysics/www/ROMY` which will publish the website. Otherwise
run `fab publish` which does it for you.

Please remember to upload to Github again - if everything went smoothly (and
nobody edited in the meanwhile):

```bash
# Add any new files
$ git add FILENAME

# Commit and push to Github.
$ git commit -a
$ git push
```

First of all make sure to pull in any potential changes made by others by doing..

```bash
$ git pull
```

### Large files

Large files that should not be commited with git (larger than 80 MB) can be
copied manually to `venus` into the directory
`/var/www/geophysics/www/ROMY/images/large_files/` (make sure to set correct
file permissions so that others can change files and everybody can read the
file) and linked in the pages managed in git.

## Configuring SSH

First step is to make sure you have a private/public key pair:
http://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/

This is useful for many things, not just the ROMY website.

Then make sure the key is copied to venus:

```bash
$ ssh-copy-id -i ~/.ssh/id_rsa.pub USERNAME@venus
```

If your local username is not identical to the geophysics one, you might also
want to add the following to your `~/.ssh/config`:

```
Host venus
    HostName venus
    User USERNAME
```

You should now be able to log-in to `venus` using a plain

```bash
$ ssh venus
```

If that works you are good to go using `fab publish`.

Data at
/import/freenas-m-www/projects/ROMY
