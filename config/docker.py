"""
Configuration file for Docker commands.

Each DOCKER entry specifies a `docker run` command that will be generated via `build.py`.

Entries are referenced by Python scripts defined in `config/scripts`. The first entry
must be named `default`. Contents are defined as follows:

    - options: `docker run` options as defined here: https://docs.docker.com/engine/reference/commandline/run/ | optional
    - image: Name of the Docker image to run | required
    - command: The base command that will be run by the Docker container | optional
    - args:  Command-line arguments to be appended to the base command. See note about $CMD below. | options

Entries support three magical vars which are replaced at build time:
- $BUILD_PATH: The absolute path to the parent directory of this repository.
    Presuming this repository shares a parent directory with the script source files,
    this makes it possible to properly mount the scripting directory regardless of where
    it is insatlled on the host.
- $CMD: This is the means by which a Python script defined in config/scripts.py is run by the
    docker container. $CMD will be replaced with the python script name and command
    arguments defined in config/scripts.py.
- $WORKDIR: The relative path defined in config/scripts.py "workdir" config. 
"""

DOCKER = {
    "default": {
        "options": ["-d", "-v $BUILD_PATH:/app", "--rm", "--network=host", "-w /app/$WORKDIR"],
        "image": "atddocker/tdp",
        "command": "python",
        "args": ["$CMD"],
    },
    "test": {
        "options": ["-v $BUILD_PATH:/app", "--rm", "--network=host", "-w /app/$WORKDIR"],
        "image": "atddocker/tdp",
        "command": "python",
        "args": ["$CMD"],
    }
}













