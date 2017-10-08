import serial

ser = serial.Serial('COM5', 9600)

myData= ser.readline().strip()
data2=myData.decode('utf-8')

data3= 9/5*(float(data2))+32
print ("temperature is:",+data3 )

if 80 <= float(data3) <= 90:
	print("Tepmperature is normal,",+data3)

elif 20 <= data3 <= 25:
	print("Tepmperature is "+data3+"  deg C the baby may be feeling cold")

else:
	print("the temperature is not acceptable for the baby")
