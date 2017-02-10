FROM python:3-alpine
RUN pip install openwhisk_docker_action
ADD script.py /
EXPOSE 5000
CMD [ "python", "./script.py" ]
