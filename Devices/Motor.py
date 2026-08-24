from time import sleep
from gpiozero import PWMOutputDevice

class Motor:
    Pulse_Check_Speed = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

    def __init__(self, Motor_Name, PIN):
        print(f"Testing: {Motor_Name} Please Wait...")

        self.Motor_Esc = PWMOutputDevice(PIN, frequency=50)

        for i in range(len(Motor.Pulse_Check_Speed)):
            self.Motor_Esc.value = Motor.Pulse_Check_Speed[i]
            sleep(1)

        print("Done Testing...")

    def Speed(self, Rot):
        self.Rot = Rot
        self.Motor_Esc.value = Rot