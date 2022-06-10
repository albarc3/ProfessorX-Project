from flask import Flask
import time
from tello_controller import TelloController

server = Flask(__name__)

@server.route('/drone/takeoff')
def droneTakeOff():
    print('taking off!!!!!!')
    controller.take_off()
    return 'Drone Taking off!!!'

@server.route('/drone/landing')
def droneLanding():
    print('landing!!!!!!')
    controller.land()
    return 'Drone landing!!!'

@server.route('/drone/moveleft')
def droneMoveLeft():
    print('moving left!!!!!!')
    controller.move_left()
    return 'Drone Moving Left!!!'

@server.route('/drone/moveright')
def droneMoveRight():
    print('moving right!!!!!!')
    controller.move_right()
    return 'Drone Moving Right!!!'

if __name__ == "__main__":

    print("--init tello controller--")
    controller = TelloController()
    controller.start()
    print("--ready--")

    time.sleep(5)

    print('--running server--')
    server.run()
