FROM secoresearch/fuseki

COPY --chown=9008 ttl/ /tmp/data/
COPY --chown=9008 load_data.sh /tmp/

# Load data
RUN /tmp/load_data.sh
