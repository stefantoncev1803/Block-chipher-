import random
import os
import sys


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


key_used = 0
key_list = []

while True:
    key = random.randint(1, 8)
    if len(key_list) == 8:
        break
    else:
        if key not in key_list:
            key_list.append(key)

key_list_2 = []
while True:
    key = random.randint(1, 5)
    if len(key_list_2) == 5:
        break
    else:
        if key not in key_list_2:
            key_list_2.append(key)

while True:
    choice = input("\nDO YOU WANT TO ENCRYPT MESSAGE : y/n ").lower()
    if choice == "n" or choice == "no":
        print("\nPROGRAM ENDED")
        break

    elif choice == "y" or choice == "yes":
        key_used += 1
        if key_used > 3:
            print("\nNEW KEY WILL BE GENERATED! PROGRAM STARTING AGAIN...... ")
            restart_program()
        else:
            print("\nKEY GENERATED: ")
            print(key_list)
        # -------------------------------------------------------------------------------
        message = input("\nPLEASE ENTER MESSAGE TO ENCRYPT: ")
        while ((len(message)) % (len(key_list)) != 0):
            message = message + " "
        print("\nORIGINAL MESSAGE: ")
        print(message)

        lenght = len(message)
        chars = int(len(key_list))
        message_list = []

        for i in range(0, lenght, chars):
            part_1 = message[i: i + chars];
            message_list.append(part_1);
        print("\nSPLITTED MESSAGE: ")
        print(message_list)

        # -------------------------------------------------------------------------------

        list_key_all = key_list * int((len(message) / len(key_list)))

        final_list = [None] * (len(message_list) * len(key_list))
        counter = 0
        counter_1000 = 0
        for i in list_key_all:
            if counter > 7:
                i = i + (8 * counter_1000)
            try:
                final_list[i - 1] = message[counter]
            except:
                IndexError
                print("out of index")

            counter += 1
            if counter % 8 == 0:
                counter_1000 += 1

        other_list = []

        for i in range(0, lenght, chars):
            part = final_list[i: i + chars];
            other_list.append(part);

        print("\nENCRYPTED MESSAGE: ")
        for i in other_list:
            print(i, end="")

        message_2 = ""
        for s in final_list:
            message_2 += s

        if (len(message_2) % len(key_list_2)) == 0:
            message_2 = message_2
        else:
            while (len(message_2) % len(key_list_2)) != 0:
                message_2 += " "

        print("\nSECOND MESSAGE IS: ")
        print(message_2)

        if key_used > 3:
            print("\nNEW KEY WILL BE GENERATED! PROGRAM STARTING AGAIN ... ")
            restart_program()

        else:
            print("\nSECOND KEY GENERETED: ")
            print(key_list_2)

        # -------------------------------------------------------------------------------

        lenght_2 = len(message_2)
        chars_2 = int(len(key_list_2))
        message_list_2 = []

        for i in range(0, lenght_2, chars_2):
            part_2 = message_2[i: i + chars_2];
            message_list_2.append(part_2);
        print("\nSPLITTED SECOND MESSAGE: ")
        print(message_list_2)

        list_key_all_2 = key_list_2 * int((len(message_2) / len(key_list_2)))

        final_list_2 = [None] * (len(message_list_2) * len(key_list_2))

        duzina = len(message_list_2)
        counter_2 = 0
        counter_2000 = 0
        for i in list_key_all_2:
            if counter_2 > 4:
                i = i + (5 * counter_2000)
            try:
                final_list_2[i - 1] = message_2[counter_2]
            except:
                IndexError
                print("out of index")

            counter_2 += 1
            if counter_2 % 5 == 0:
                counter_2000 += 1

        other_list_2 = []

        for i in range(0, lenght_2, chars_2):
            part_2 = final_list_2[i: i + chars_2];
            other_list_2.append(part_2);

        print("ENCRYPTED MESSAGE SECOND TIME: ")
        for i in other_list_2:
            print(i, end="")
        message_3 = ""
        for i in final_list_2:
            message_3 += i
        print("\n", message_3)

        print("\nDECRYPTING SECOND MESSAGE......")
        print()
        counter_3 = 0
        counter_3000 = 0

        second_list_decripted = [None] * (len(message_list_2) * len(key_list_2))

        for i in list_key_all_2:
            if counter_3 > 4:
                i = i + (5 * counter_3000)
            try:
                second_list_decripted[counter_3] = final_list_2[i-1]
            except IndexError:
                print("out of index")

            counter_3 += 1
            if counter_3 % 5 == 0:
               counter_3000 += 1
        print("\nSECOND MESSAGE DECRYPTED: ")
        for i in second_list_decripted:
            print(i,end="")
#---------------------------------------------------------------------------
        decrypted_list = second_list_decripted
        while len(second_list_decripted) > len(final_list):
            decrypted_list.reverse()
            try:
                decrypted_list.remove(" ")
            except:
                ValueError
            decrypted_list.reverse()

        counter_4 = 0
        counter_4000 = 0

        first_list_decripted = [None] * (len(message_list) * len(key_list))

        #
        for i in list_key_all:
            if counter_2 > 7:
                i = i + (8 * counter_4000)
            try:
                first_list_decripted[counter_4] = decrypted_list[i-1]
            except IndexError:
                print("out of index")

            counter_4 += 1
            if counter_4 % 8 == 0:
                counter_4000 += 1
        print("\nFIRST MESSAGE DECRYPTED: ")
        for i in first_list_decripted:
            print(i, end="")


    else:
        print("Please enter valid choice")

