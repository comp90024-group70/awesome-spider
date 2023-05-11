FROM python:3.11.3-alpine3.16
WORKDIR /app
COPY ../requirements.txt /app
COPY ../db.py /app
COPY ../MAS_AU.py /app
RUN pip install -r requirements.txt
EXPOSE 8010
CMD ["python3", "MAS_AU.py"]