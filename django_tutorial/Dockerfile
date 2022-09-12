FROM python:3.8
RUN mkdir /workspace && chown -R 42420:42420 /workspace
ENV HOME /workspace
WORKDIR /workspace
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /workspace
RUN pip install -r requirements.txt
CMD [ "python3" , "manage.py" , "runserver"]