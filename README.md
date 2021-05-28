# binder-demo-template

## About this template 

This template can be used to create SNAP based notebooks to be demoed or exploited on Binder.

## Using this template

### Update the conda dependencies

Create a file named `environment.yml` with the additional conda dependencies:

Below an example

```yaml
channels:
 - conda-forge
dependencies:
 - <your conda package>
```

### Update other dependencies

Edit the file `.binder/Dockerfile` and add the additional tools with `apt`.

Example:

```
FROM terradue/docker-snap-binder:latest

USER root
# install additional packages here

RUN apt-get install tree

USER jovyan

COPY --chown=jovyan:jovyan . /home/jovyan

RUN test -f ${HOME}/environment.yml && mamba env update -p /srv/conda/envs/env_snap -f ${HOME}/environment.yml  && \
    test -f ${HOME}/postBuild && chmod +x ${HOME}/postBuild && ${HOME}/postBuild || exit 0
```

### Testing the docker image 

You can test the docker image before pushing your changes to GitHub with:

```console
docker build -f .binder/Dockerfile -t img-test .
```

And once built, do:

```console
docker run --rm -it -p 8888:8888 -v $PWD:/home/jovyan img-test:latest jupyter lab --port=8888 --ip=0.0.0.0 --NotebookApp.token='' --no-browser
```

And open a browser tab at http://0.0.0.0:8888/lab

<hr>

Now delete everything above and create your README here.
Don't forget to update the Binder URL

## Run me on Binder 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/snap-contrib/binder-demo-template/HEAD)
