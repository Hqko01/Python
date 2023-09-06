import pywhatkit as kit

try:
    kit.sendwhatmsg("numara", "mesaj", 15,59)
except:
    print('Hata Oluştu')
