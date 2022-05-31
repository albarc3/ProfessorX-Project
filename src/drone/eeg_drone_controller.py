"""
Demo the trick flying for the python interface

Author: Amy McGovern
"""

# from pyparrot.Minidrone import Mambo
from vendor.Minidrone import Mambo


class DroneController:
    mamboAddrStatic = "e0:14:0c:71:3d:fc"

    def __init__(self):
        print("simple init")

    def start(self):
        print("start drone controller")
        self.verticalCount = 0
        self.horizontalCount = 0
        self.deepCount = 0
        self.mamboAddr = "e0:14:0c:71:3d:fc"
        #self.mambo = Mambo(self.mamboAddr, use_wifi=False)
        self.mambo = Mambo(self.mamboAddrStatic, use_wifi=False)
        self.success = self.mambo.connect(num_retries=3)

    def moveRight(self):
        print(f"/nmoveRight")
        # global horizontalCount
        # global self.mambo
        print("horizontalCount: " + str(self.horizontalCount))
        if abs(self.horizontalCount) < 5:
            self.mambo.fly_direct(roll=15, pitch=0, yaw=0, vertical_movement=0, duration=1)
            self.horizontalCount = self.horizontalCount + 1
            self.mambo.smart_sleep(1)

    def takeOff(self):
        print(f"/ntakeOff")
        self.mambo.safe_takeoff(5)


    def safeLand(self):
        self.mambo.safe_land(5)
        print(f"/nsafeLand")


    def moveLeft(self):
        print(f"/nmoveLeft")
        global horizontalCount
        global mambo
        print("horizontalCount: " + str(horizontalCount))
        if abs(horizontalCount) < 5:
            mambo.fly_direct(roll=-15, pitch=0, yaw=0, vertical_movement=0, duration=1)
            self.horizontalCount = horizontalCount - 1
            mambo.smart_sleep(1)

    def moveForward(self):
        print(f"/nmoveForward")
        global deepCount
        global mambo
        print("deepCount: " + str(deepCount))
        if abs(deepCount) < 5:
            mambo.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=1)
            self.deepCount = deepCount + 1
            mambo.smart_sleep(1)

    def moveBackward(self):
        print(f"/nmoveBackward")
        global deepCount
        global mambo
        print("deepCount: " + str(deepCount))
        if abs(deepCount) < 5:
            mambo.fly_direct(roll=0, pitch=-20, yaw=-0, vertical_movement=0, duration=1)
            self.deepCount = deepCount + 1
            mambo.smart_sleep(1)

    def moveUp(self):
        print(f"/nmoveUp")
        global verticalCount
        global mambo
        print("verticalCount: " + str(verticalCount))
        if abs(verticalCount) < 5:
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=1)
            self.verticalCount = verticalCount + 1
            mambo.smart_sleep(1)

    def moveDown(self):
        print(f"/nmoveDown")
        global verticalCount
        global mambo
        print("verticalCount: " + str(verticalCount))
        if abs(verticalCount) < 5:
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=1)
            self.verticalCount = verticalCount - 1
            mambo.smart_sleep(1)

    def rotateRight(self):
        global mambo
        print(f"/nrotateRight")
        mambo.fly_direct(roll=0, pitch=0, yaw=10, vertical_movement=0, duration=1)
        mambo.smart_sleep(1)

    def rotateLeft(self):
        global mambo
        print(f"/nrotateLeft")
        mambo.fly_direct(roll=0, pitch=0, yaw=-10, vertical_movement=0, duration=1)
        mambo.smart_sleep(1)

    def takeOff(self):
        mambo.safe_takeoff(5)
        print(f"/ntakeOff")

    def safeLand(self):
        mambo.safe_land(5)
        print(f"/nsafeLand")

    def fire(self):
        mambo.fire_gun()
        print(f"/nfire")
    

