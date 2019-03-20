import RPi.GPIO as LCD
import time

LCD_RS = 40
LCD_E  = 38
LCD_D4 = 37
LCD_D5 = 35
LCD_D6 = 33
LCD_D7 = 31

LCD_WIDTH = 16
LCD_CHAR = True
LCD_CMD = False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0


E_PULSE = 0.0005
E_DELAY = 0.0005

def main ():
    LCD.setwarnings(False)
    LCD.setmode(LCD.BOARD)
    LCD.setup(LCD_E, LCD.OUT)
    LCD.setup(LCD_RS, LCD.OUT)
    LCD.setup(LCD_D4, LCD.OUT)
    LCD.setup(LCD_D5, LCD.OUT)
    LCD.setup(LCD_D6, LCD.OUT)
    LCD.setup(LCD_D7, LCD.OUT)
    
    lcd_init()
    lcd_byte(0x01, LCD_CMD)
    
    lcd_string("    Welcome", LCD_LINE_1)
    lcd_byte(0x01, LCD_CMD)
    
    lcd_string("    to mbcet", LCD_LINE_2)
    while True:
        time.sleep(1)
        
def lcd_init():
    
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)
    
def lcd_byte(bits, mode):
    
    
    LCD.output(LCD_RS, mode)
    
    for i in range(2):
        for i in [LCD_D4, LCD_D5, LCD_D6, LCD_D7]:
            LCD.output(i, False)
            
        if bits&0x01 == 0x02:
            LCD.output(LCD_D4, True)
        if bits&0x02 == 0x02:
            LCD.output(LCD_D5, True)
        if bits&0x04 == 0x04:
            LCD.output(LCD_D6, True)
        if bits&0x08 == 0x08:
            LCD.output(LCD_D7, True)
        
        lcd_toggle_enable()
        
def lcd_toggle_enable():
    
    time.sleep(E_DELAY)
    LCD.output(LCD_E, True)
    time.sleep(E_PULSE)
    LCD.output(LCD_E, False)
    time.sleep(E_DELAY)
    
def lcd_string(message, line):
    
    message = message.ljust(LCD_WIDTH, " ")
    
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHAR)
        
        
main()
if __name__ == "__main__":
    
   try:
       main()
   except KeyboardInterrupt:
        pass
   finally:
       LCD.cleanup()