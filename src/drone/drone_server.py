from flask import Flask

server = Flask(__name__)

@server.route('/drone/takeoff')
def DroneMoveRight():
    return 'Drone Taking off!!!'

@server.route('/drone/landing')
def DroneMoveRight():
    return 'Drone landing!!!'

@server.route('/drone/left')
def DroneMoveLeft():
    return 'Drone Moving Left!!!'

@server.route('/drone/right')
def DroneMoveRight():
    return 'Drone Moving Right!!!'

@server.route('/drone/fire')
def DroneMoveRight():
    return 'Drone firing!!!'