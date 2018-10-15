# Toolpath Analysis

A basic program to perform Data analysis on gcode files. Currently it can handle small gcode files of upto 100,000 lines well. Larger gcode files might have performance issues.
It is currently compatible with Simplify3D gcodes of version 4.X

The purpose of this program is to visualize the gcode data in the form of charts and graphs. This tool will allow us to understand the components of the 3D Printed part using vidual tools

## Installation and Dependencies

This program is pretty much a script at this point. It is written in Python.


## Dependencies

The program is written in Python. It is compatible with the 3.5 and higher
The Python libraries required to get this program going are 

Pandas
Numpy
re
math
Matplotlib
Seaborn
Pathlib

All these libraries can be installed using `pip`
    pip install 

## Usage



![Screenshot](https://i.imgur.com/7FmlIRp.png)


![Screenshot](https://i.imgur.com/IPPJmSJ.png)

You are currently looking at the source code repository of OctoPrint. If you already installed it
(e.g. by using the Raspberry Pi targeted distribution [OctoPi](https://github.com/guysoft/OctoPi)) and only
want to find out how to use it, [the documentation](http://docs.octoprint.org/) and [the public wiki](https://github.com/foosel/OctoPrint/wiki)
might be of more interest for you. You might also want to subscribe to join 
[the community forum at discourse.octoprint.org](https://discourse.octoprint.org) where there are other active users who might be
able to help you with any questions you might have.

## Installation

Installation instructions for installing from source for different operating
systems can be found [on the wiki](https://github.com/foosel/OctoPrint/wiki#assorted-guides).

If you want to run OctoPrint on a Raspberry Pi, you might want to take a look at [OctoPi](https://github.com/guysoft/OctoPi)
which is a custom SD card image that includes OctoPrint plus dependencies.

The generic steps that should basically be done regardless of operating system
and runtime environment are the following (as *regular
user*, please keep your hands *off* of the `sudo` command here!) - this assumes
you already have Python 2.7, pip and virtualenv set up on your system:

1. Checkout OctoPrint: `git clone https://github.com/foosel/OctoPrint.git`
2. Change into the OctoPrint folder: `cd OctoPrint`
3. Create a user-owned virtual environment therein: `virtualenv venv`
4. Install OctoPrint *into that virtual environment*: `./venv/bin/pip install .`

You may then start the OctoPrint server via `/path/to/OctoPrint/venv/bin/octoprint`, see [Usage](#usage)
for details.

After installation, please make sure you follow the first-run wizard and set up
access control as necessary. 

## Dependencies

OctoPrint depends on a few python modules to do its job. Those are automatically installed when installing
OctoPrint via `pip`:

    pip install .

You should do this every time after pulling from the repository, since the dependencies may have changed.

OctoPrint currently only supports Python 2.7.

## Usage

Running the pip install via

    pip install .

installs the `octoprint` script in your Python installation's scripts folder
(which, depending on whether you installed OctoPrint globally or into a virtual env, will be in your `PATH` or not). The
following usage examples assume that the `octoprint` script is on your `PATH`.

You can start the server via

    octoprint serve

By default it binds to all interfaces on port 5000 (so pointing your browser to `http://127.0.0.1:5000`
will do the trick). If you want to change that, use the additional command line parameters `host` and `port`,
which accept the host ip to bind to and the numeric port number respectively. If for example you want the server
to only listen on the local interface on port 8080, the command line would be

    octoprint serve --host=127.0.0.1 --port=8080

Alternatively, the host and port on which to bind can be defined via the config file.

If you want to run OctoPrint as a daemon (only supported on Linux), use

    octoprint daemon {start|stop|restart} [--pid PIDFILE]

If you do not supply a custom pidfile location via `--pid PIDFILE`, it will be created at `/tmp/octoprint.pid`.

You can also specify the config file or the base directory (for basing off the `uploads`, `timelapse` and `logs` folders),
e.g.:

    octoprint serve --config /path/to/another/config.yaml --basedir /path/to/my/basedir

To start OctoPrint in safe mode - which disables all third party plugins that do not come bundled with OctoPrint - use
the ``--safe`` flag:

    octoprint serve --safe

See `octoprint --help` for more information on the available command line parameters.

OctoPrint also ships with a `run` script in its source directory. You can invoke it to start the server. It
takes the same command line arguments as the `octoprint` script.

## Configuration

If not specified via the command line, the config file `config.yaml` for OctoPrint is expected in the settings folder,
which is located at `~/.octoprint` on Linux, at `%APPDATA%/OctoPrint` on Windows and
at `~/Library/Application Support/OctoPrint` on MacOS.

A comprehensive overview of all available configuration settings can be found
[in the docs](http://docs.octoprint.org/en/master/configuration/config_yaml.html).
Please note that the most commonly used configuration settings can also easily
be edited from OctoPrint's settings dialog.

## Special Thanks

Cross-browser testing services are kindly provided by [BrowserStack](http://www.browserstack.com/).
Profiling is done with the help of [PyVmMonitor](http://www.pyvmmonitor.com).
