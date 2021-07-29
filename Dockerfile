FROM python:3.9.2-alpine

RUN pip install schedule
RUN pip install pyyaml

RUN mkdir /yaml
RUN mkdir /entry

ADD util.py /entry/
ADD configInit.py /entry/
ADD main.py /entry/

WORKDIR /entry/
CMD [ "python", "-u", "main.py" ]