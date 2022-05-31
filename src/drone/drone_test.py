from vendor.Minidrone import Mambo
from eeg_drone_controller import DroneController


def main():
    print("init drone test")
    controller = DroneController()

    controller.start()
    controller.takeOff()
    controller.safeLand()


if __name__ == "__main__":
    main()
