FROM terradue/docker-snap:latest

USER root
RUN usermod -u 1000 jovyan   && \
    groupmod -g 1000 jovyan

RUN chown -R jovyan:jovyan /srv/conda
RUN chown -R jovyan:jovyan /home/jovyan

RUN mamba install -n env_snap ipykernel snapista

ADD .binder/environment.yml /tmp/environment.yml

RUN mamba env update -p /srv/conda -f /tmp/environment.yml

EXPOSE 8888

WORKDIR /home/jovyan

USER jovyan
