import serial               #import serial pacakge
from time import sleep
ser = serial.Serial ("/dev/ttyS0", baudrate=9600, timeout=0.5)
gpgga_info = "$GPGGA,"
f = open("gps_data.txt", "w")
while True:
        received_data = str(ser.readline())
        print(received_data)
        GPGGA_data_available = received_data.find(gpgga_info)
        if (GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
            NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
            #print(NMEA_buff )
            nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
            nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
            nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
            
#             nmea_latitude = float(nmea_latitude )
#             nmea_longitude  = float(nmea_longitude  )
            print("NMEA Time: ", nmea_time,'\n')
            print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
            f.write(nmea_latitude + ","+ nmea_longitude)
            
        sleep(1)
f.close()
