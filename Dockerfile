FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /twassign
ADD . /twassign
COPY ./requirements.txt /twassign/requirements.txt
RUN pip install -r requirements.txt
COPY . /twassign
EXPOSE 8000
CMD python manage.py runserver 0:8000
