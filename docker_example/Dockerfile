FROM python:3-alpine
RUN pip install openwhisk_docker_action
RUN pip install watson_developer_cloud
ADD script.py /
EXPOSE 8080
CMD [ "python", "./script.py" ]
