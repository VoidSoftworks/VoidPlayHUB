from Pop_up import *
from dialoge import *



def Initiate_encounter():
    Action = input ('\n' "Wold you like to go into the room?"'\n''\n' "-yes-"'\n'"-no-"'\n').lower()
    if Action == "yes":
        Encounter_display()
    elif Action == "no":
        print ("Too Bad!")
        Encounter_display()
    else:
        print ("invalid Action")
        Initiate_encounter()






if __name__ == "__main__":
    Initiate_encounter()
