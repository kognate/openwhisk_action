from openwhisk_docker_action import Action


app = Action('My Openwhisk Action')

@app.main
def main(params):
    return {'hello': 'world'}
