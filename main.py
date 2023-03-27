def on_button_pressed_a():
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
        kitronik_motor_driver.MotorDirection.FORWARD,
        97)
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
        kitronik_motor_driver.MotorDirection.FORWARD,
        100)
    basic.pause(1000)
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
input.on_button_pressed(Button.A, on_button_pressed_a)