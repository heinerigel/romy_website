# Romy Website

## Installing the Dependencies

Python should already be installed on most systems.


```bash
# Install pip if not available
$ sudo apt-get install python-pip

# Install pelican
$ pip install pelican
$ pip install markdown

# Install fabric for the deployment
$ pip install fabric
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

Creates the final HTML files in the `output/` subdirectory.

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
