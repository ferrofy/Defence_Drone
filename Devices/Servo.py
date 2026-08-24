from gpiozero import AngularServo
from time import sleep

class Servo:
    def __init__(self, PIN, Min, Max):
        print("Testing Servo...")

        self.Servo_Motor = AngularServo(PIN, min_angle=Min, max_angle=Max)
        self.Min = Min
        self.Max = Max

        Angle_Difference = Max - Min

        for i in range(0, 5):
            if i == 0:
                print(f"Checking Servo So, Doing At Min Angle Which Is: {Min}°")
                self.Servo_Motor.angle = Min
                sleep(0.7)
                print("Done...")

            else:
                Angle = int(Min + (Angle_Difference / 4) * i)
                print(f"Doing Servo At Angle {Angle}°")
                self.Servo_Motor.angle = Angle
                sleep(0.3)
                print("Done...")

        print(f"Reaching Maximum Angle Which Is: {Max}°, After This Aiming At {Min}°")
        self.Servo_Motor.angle = Max
        sleep(0.7)

        self.Servo_Motor.angle = Min
        sleep(0.7)

        print("Done Testing...")

    def Angle(self, Angle):
        self.Servo_Motor.angle = Angle