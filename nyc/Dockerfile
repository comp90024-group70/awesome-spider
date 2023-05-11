FROM python:3.11.3-alpine3.16
WORKDIR /app
COPY ../requirements.txt /app
COPY ../db.py /app
COPY ../MAS_NYC.py /app
RUN pip install -r requirements.txt
EXPOSE 8011
CMD ["python3", "MAS_NYC.py"]