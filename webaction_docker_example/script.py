from openwhisk_docker_action import Action

app = Action('My Openwhisk Action', methods=['GET'])

@app.web
def main(params):
    return 200, 'text/html', "<html><body><h1>Hello World</h1></body></html>"
