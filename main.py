from Devices.Motor import Motor
from Devices.Servo import Servo
from Devices.Tilt_Sensor import Tilt

print("Starting Drone... Gathering And Testing Parts...")
print("Testing Motors...")

Motor_1 = Motor("1st" , 18)
Motor_1.Rot(0.05)
Motor_2 = Motor("2nd" , 12)
Motor_2.Rot(0.05)
Motor_3 = Motor("3rd" , 13)
Motor_3.Rot(0.05)
Motor_4 = Motor("4th" , 19)
Motor_4.Rot(0.05)

print("Testing And Defining Tilt Angle...")

Tilt_Angle = Tilt() # Pin 3 And Pin 5

print("Testing Servos To Aim Guns...")

Gun_360 = Servo(23, 0, 360)
Gun_Y = Servo(24 , 0, 45)

Proceed = input("All Devices Motion Checked Press Enter To Start ?")
print("Starting Motors")

while True:
    Set_Speed = 0.06
    Motor_1.Speed(Set_Speed)
    Motor_2.Speed(Set_Speed)
    Motor_3.Speed(Set_Speed)
    Motor_4.Speed(Set_Speed)
    Check = input("Is Flying And Close To Stable [Y/n] ?")
    print(f"Power Set To {Set_Speed * 100} %")
    if Check.lower() == "y":
        break
    else:
        if Set_Speed < 0.1:
            Set_Speed += Set_Speed + 0.01
        else:
            print("Your Max Speed Leached. Exiting...")
            break

# Threshold_Angle = 5

# while True:
#     X = Tilt_Angle.X_Angle
#     Y = Tilt_Angle.Y_Angle

#     if X > Threshold_Angle or Y > Threshold_Angle:
#         if X > Threshold_Angle:
#             pass
#         else:
#             pass
