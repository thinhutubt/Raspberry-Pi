import RPi.GIPO as GPIO #Them thu vien RPI.GPIO va goi lai voi ten la GPIO


GPIO.setmode(GPIO.BOARD) #So chan GPIO tu 1 --> 40
#Cach khai bao khac
#GPIO.setmode(GPIO.BCM) #So chan GPIO theo ten GPIO, vi du: GPIO27

PIN1 = 7 #Ta muon no la chan INPUT
PIN2 = 11 #Ta muon no la chan OUTPUT

GPIO.setup(PIN1, GPIO.IN) #PIN1 thanh PIN INPUT
GPIO.setup(PIN2, GPIO.OUT) #PIN2 thanh PIN OUTPUT
#Mot so ung dung ta can dien tro treo (dien tro pullup len nguon)

#Doc tin hieu vao tu chan PIN1 - chan INPUT
Signal_INPUT = GPIO.input(PIN1) #Ket qua doc vao la 0 hoac 1

#Xuat tin hieu muc cao ra chan PIN2 - chan OUTPUT
Signal_OUTPUT = GPIO.output(PIN2,1)#true hoac 1: muc cao; false hoac 0: muc thap
