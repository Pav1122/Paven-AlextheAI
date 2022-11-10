import datetime
import playsound
import winsound
import Annex
def alarm (Timing):
    alttime= str(datetime.datetime.now().strptime(Timing,'%I:%M %p'))
    alttime = alttime[11:-3]
    Horeal = alttime[:2]
    Horeal=int(Horeal)
    Mireal =alttime[3:5]
    Mireal=int(Mireal)

    while (True):
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                winsound.PlaySound('abc',winsound.SND_LOOP)
                continue
            elif Mireal < datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm('')





