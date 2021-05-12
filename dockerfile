FROM python:3.8-alpine

MAINTAINER Peter Cort "petercort@gmail.com"

COPY requirements.txt . 
RUN mkdir -p ProjectEuler/
RUN pip3 install -r requirements.txt

COPY ProjectEuler ProjectEuler/ProjectEuler

WORKDIR /ProjectEuler

CMD [ "pip3 install -e ."]
ENV FLASK_APP=ProjectEuler
ENV FLASK_ENV=development

EXPOSE 5000
CMD [ "python3", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]