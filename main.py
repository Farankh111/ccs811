oledssd1306.init_display()
oledssd1306.turn_on()
oledssd1306.clear_display()
gatorEnvironment.begin_environment()
C = gatorEnvironment.measurement(MeasurementType.DEGREES_C)
basic.pause(5000)

def on_forever():
    global C
    oledssd1306.set_text_xy(0, 1)
    oledssd1306.write_string("Temp:")
    C += gatorEnvironment.measurement(MeasurementType.DEGREES_C)
    oledssd1306.write_number(C)
    basic.pause(2000)
basic.forever(on_forever)
