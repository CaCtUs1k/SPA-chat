FROM python:3.11-slim
LABEL maintainer="denischernish19012004@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DEBUG_MODE False
ENV SECRET_KEY "mysecretkey"
ENV GOOGLE_RECAPTCHA_SECRET_KEY "6Le-pC4pAAAAAIKqpABdttoCeZf2waJ08GAphOKl"
ENV GOOGLE_RECAPTCHA_PUBLIC_KEY "6Le-pC4pAAAAAH1Duy4ieCg6_Tm6OMhbE-CmsedQ"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]