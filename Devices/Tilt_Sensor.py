import math
from smbus2 import SMBus

class Tilt:
    def __init__(self):
        print("Starting Tilt Sensor")
        print("Checking Sensor Data")

        self.Address = 0x53

        self.Register_Data_Format = 0x31
        self.Register_Bw_Rate = 0x2C
        self.Register_Power_Ctl = 0x2D
        self.Register_Data_X0 = 0x32

        self.Gravity = 9.80665

        self.X_Angle = 0
        self.Y_Angle = 0
        self.Total_Tilt = 0

        print(f"X : {self.X_Angle}°")
        print(f"Y : {self.Y_Angle}°")
        print("Done...")

    def Check_Tilt(self):
        Bus = SMBus(1)

        Bus.write_byte_data(
            self.Address,
            self.Register_Data_Format,
            0x08
        )

        Bus.write_byte_data(
            self.Address,
            self.Register_Bw_Rate,
            0x0A
        )

        Bus.write_byte_data(
            self.Address,
            self.Register_Power_Ctl,
            0x08
        )

        Data = Bus.read_i2c_block_data(
            self.Address,
            self.Register_Data_X0,
            6
        )

        X_Raw = int.from_bytes(
            bytes([Data[0], Data[1]]),
            byteorder="little",
            signed=True
        )

        Y_Raw = int.from_bytes(
            bytes([Data[2], Data[3]]),
            byteorder="little",
            signed=True
        )

        Z_Raw = int.from_bytes(
            bytes([Data[4], Data[5]]),
            byteorder="little",
            signed=True
        )

        X_G = X_Raw * 0.0039
        Y_G = Y_Raw * 0.0039
        Z_G = Z_Raw * 0.0039

        X_Acc = X_G * self.Gravity
        Y_Acc = Y_G * self.Gravity
        Z_Acc = Z_G * self.Gravity

        self.X_Angle = round(
            math.degrees(
                math.atan2(
                    X_Acc,
                    math.sqrt(
                        Y_Acc ** 2 +
                        Z_Acc ** 2
                    )
                )
            ),
            1
        )

        self.Y_Angle = round(
            math.degrees(
                math.atan2(
                    Y_Acc,
                    math.sqrt(
                        X_Acc ** 2 +
                        Z_Acc ** 2
                    )
                )
            ),
            1
        )

        self.Total_Tilt = round(
            math.sqrt(
                self.X_Angle ** 2 +
                self.Y_Angle ** 2
            ),
            1
        )
        Bus.close()


# Tilt_Sensor = Tilt()

# Tilt_Sensor.Check_Tilt()

# X = Tilt_Sensor.X_Angle
# Y = Tilt_Sensor.Y_Angle
# Total = Tilt_Sensor.Total_Tilt

# print (X , Y , Total)