class LCD_Display:

    def __init__(self, RS=40, E=38, D4=37, D5=35, D6=33, D7=31, WIDTH=16, LINE_1=0x80, LINE_2=0xC0):
        import RPi.GPIO as LCD
        import time

        self.LCD_RS = RS
        self.LCD_E  = E
        self.LCD_D4 = D4
        self.LCD_D5 = D5
        self.LCD_D6 = D6
        self.LCD_D7 = D7

        self.LCD_WIDTH = WIDTH
        self.LCD_CHAR = True
        self.LCD_CMD = False

        self.LCD_LINE_1 = LINE_1
        self.LCD_LINE_2 = LINE_2


        self.E_PULSE = 0.0005
        self.E_DELAY = 0.0005

        LCD.setwarnings(False)
        LCD.setmode(LCD.BOARD)
        LCD.setup(self.LCD_E, LCD.OUT)
        LCD.setup(self.LCD_RS, LCD.OUT)
        LCD.setup(self.LCD_D4, LCD.OUT)
        LCD.setup(self.LCD_D5, LCD.OUT)
        LCD.setup(self.LCD_D6, LCD.OUT)
        LCD.setup(self.LCD_D7, LCD.OUT)

        self.lcd_byte(0x33, LCD_CMD)
        self.lcd_byte(0x32, LCD_CMD)
        self.lcd_byte(0x06, LCD_CMD)
        self.lcd_byte(0x0C, LCD_CMD)
        self.lcd_byte(0x28, LCD_CMD)
        self.lcd_byte(0x01, LCD_CMD)
        time.sleep(self.E_DELAY)

    def lcd_byte(self, bits, mode):
        
        
        LCD.output(self.LCD_RS, mode)
        
        for i in range(2):
            for i in [self.LCD_D4, self.LCD_D5, self.LCD_D6, self.LCD_D7]:
                LCD.output(i, False)
                
            if bits&0x01 == 0x02:
                LCD.output(self.LCD_D4, True)
            if bits&0x02 == 0x02:
                LCD.output(self.LCD_D5, True)
            if bits&0x04 == 0x04:
                LCD.output(self.LCD_D6, True)
            if bits&0x08 == 0x08:
                LCD.output(self.LCD_D7, True)
            
            self.lcd_toggle_enable()
            
    def lcd_toggle_enable(self):
        
        time.sleep(self.E_DELAY)
        LCD.output(self.LCD_E, True)
        time.sleep(self.E_PULSE)
        LCD.output(self.LCD_E, False)
        time.sleep(self.E_DELAY)
        
    def lcd_string(self, message, line):
        
        message = message.ljust(self.LCD_WIDTH, " ")
        
        self.lcd_byte(line, self.LCD_CMD)
        for i in range(self.LCD_WIDTH):
            self.lcd_byte(ord(message[i]), self.LCD_CHAR)
            
            
if __name__ == "__main__":
    Disp = LCD_Display()
    try:
        Disp.lcd_string("    Welcome", Disp.LCD_LINE_1)
        Disp.lcd_string("   To MBCET", Disp.LCD_LINE_2)
    except KeyboardInterrupt:
        pass
    finally:
        LCD.cleanup()