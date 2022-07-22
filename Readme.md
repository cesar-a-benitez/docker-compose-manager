# Docker Compose Manager

## Summary

* [About](#about)
* [Usage](#usage)
* [Options](#options)
* [Troubleshoting](#troubleshoting)

## About

This project was created using `python3` and was created as a helper in the development and maintenance of docker-compose based projects.

## Usage

1. Copy the files in this directory
1. Navigate to a project diretory that has a `docker-compose`file (Works with `.yaml` and `.yml`)
1. Paste the files in the project diretory
1. Open this directory on a shell
1. Type the following command, replasing `${CMD}` for the options you want to use
    1. `./manager ${CMD}`

### Options

| Option | Description |
|:------:|-------------|
**-h**<br>**--help** | Show a help message, listing all the options
**-d**<br>**--deploy** | Deploys all the services<br>Equivalent of `docker-compose up -d`
**-u**<br>**--update** | This option requires a service name that will be updated<br>If all the services needs to be updated pass `all` as the service name<br><br>***PS.: This command will update service by service rebuilding and recreating each service***
**-l**<br>**--list** | This option will list all the services contained in the `docker-compose` file
**-i**<br>**--info** | This option will print the service name, container name and image or if needs to be built information of each service of the `docker-compose` file<br>
**-ns**<br>**--no-spinner** | Disables the spinner indicator

## Troubleshoting

* If the command `./manager` doesn't work it's probably caused by the python not beeing in the path `/usr/bin/python`, if so you can try to run with `python manager`