FROM python:3.11.3-alpine3.16
WORKDIR /app
COPY requirements.txt /app
COPY db.py /app
COPY MAS_AU.py /app
ARG COUCHDB_DOMAIN
ENV COUCHDB_DOMAIN $COUCHDB_DOMAIN
ARG COUCHDB_USER
ENV COUCHDB_USER $COUCHDB_USER
ARG COUCHDB_PASSWORD
ENV COUCHDB_PASSWORD $COUCHDB_PASSWORD
RUN pip install -r requirements.txt
EXPOSE 8010
CMD ["python3", "MAS_AU.py"]