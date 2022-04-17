FROM ibmcom/websphere-traditional:8.5.5.21

# log basic instead of json
ENV ENABLE_BASIC_LOGGING=true

COPY --chown=was:root webapp-1.0-SNAPSHOT.war /work
COPY --chown=was:root was-conf/ /work/config/

RUN /work/configure.sh