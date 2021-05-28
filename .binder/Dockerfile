FROM terradue/docker-snap-binder:latest

USER root
# install additional packages here
RUN apt-get install tree

RUN chown -R jovyan:jovyan /srv/conda

USER jovyan

COPY --chown=jovyan:jovyan . /home/jovyan

RUN test -f ${HOME}/environment.yml && mamba env update -p /srv/conda/envs/env_snap -f ${HOME}/environment.yml  && \
    test -f ${HOME}/postBuild && chmod +x ${HOME}/postBuild && ${HOME}/postBuild || exit 0
