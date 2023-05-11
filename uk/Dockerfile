FROM python:3.11.3-alpine3.16
WORKDIR /app
COPY requirements.txt /app
COPY db.py /app
COPY MAS_UK.py /app
RUN pip install -r requirements.txt
EXPOSE 8012
CMD ["python3", "MAS_UK.py"]