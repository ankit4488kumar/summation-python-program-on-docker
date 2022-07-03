# Dockerfile, Image, Container
FROM python:3.8

ADD main.py .

#RUN pip install <package name that you wanted to be installed>

COPY . /app

CMD ["python","./main.py"]
