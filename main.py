dist=0
rawdist=0
pins.digital_write_pin(DigitalPin.P15,1)
basic.pause(500)
set_dist=15

while(True):
    pins.digital_write_pin(DigitalPin.P15,0)
    pins.digital_write_pin(DigitalPin.P15,1)
    basic.pause(200)
    rawdist=pins.analog_read_pin(AnalogPin.P2)
    dist=rawdist*1.1
    basic.show_number(dist)
    basic.pause(500)
    if dist < set_dist:
        input.running_time()
        kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
        kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
