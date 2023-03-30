dist=0
rawdist=0
pins.digital_write_pin(DigitalPin.P15,1)
basic.pause(500)
set_dist=10
time1=0

while(True):
    pins.digital_write_pin(DigitalPin.P15,0)
    pins.digital_write_pin(DigitalPin.P15,1)
    basic.pause(200)
    rawdist=pins.analog_read_pin(AnalogPin.P2)
    dist=rawdist*1.1
    basic.pause(500)
    for i in range(4):
        if dist > set_dist:
            input.running_time()
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1, kitronik_motor_driver.MotorDirection.FORWARD, 20)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2, kitronik_motor_driver.MotorDirection.FORWARD, 20)
