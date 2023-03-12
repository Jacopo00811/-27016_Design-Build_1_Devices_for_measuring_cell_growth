import time
from machine import Pin, ADC
import math

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

led = Pin(27,Pin.IN)
safe_led = Pin(12, Pin.OUT)

Running = True
safe_led.on()
Ref = 2900
av_OD = 0
raw_low = 0.06754080
raw_high = 0.5300517
ref_low = 0 

ref_high = 1.304
raw_range = raw_high - raw_low
ref_range = ref_high - ref_low

time.sleep(7)

if led.value() == 0:
    safe_led.off()
    time.sleep(2)
    safe_led.on()
    
    
    while Running == True:
    
   
        with open('data.txt', 'a') as file: 
            for i in range(50):
                od = -math.log10(adc.read()/Ref)
                av_OD = av_OD + od
                time.sleep(0.3)
            
        
            OD = av_OD/50
            av_OD = 0
        
            fixed_OD = (((OD-raw_low)*ref_range)/raw_range)+ref_low
            print(fixed_OD)
            file.write(str(fixed_OD)+"\n")
            file.close()
        
        for i in range(45):
            time.sleep(1)
            if led.value()== 1:
                pass
            else:
                Running = False
                break
        
       
    safe_led.off()
    print("It is safe to unplug the device")

else:
    for i in range(10):
        safe_led.off()
        time.sleep(1)
        safe_led.on()
        time.sleep(1)
    