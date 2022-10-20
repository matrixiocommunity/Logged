import os
import pickle
import time
import sys
import shutil
from cryptography.fernet import Fernet
os.system('color 0A')


def dres():
    if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database"):
        shutil.rmtree("C:\\Users\\Public\\Documents\\Logged Database")


def display(mem_key, log_key):
    os.system('cls')
    try:
        key = load_key()
        decrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(mem_key) + "dot" + str(log_key) + ".lg",
                key)
    except:
        pass
    with open("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(mem_key) + "dot" + str(log_key) + ".lg",
              "rb") as f:
        os.system('cls')
        print("\n", users[mem_key], "'s", logs[log_key], "as logged:\n")
        ct = 1
        pickle.load(f)
        while 1:
            try:
                print("", ct, ":    ", pickle.load(f), end="")
                ct = ct + 1
            except EOFError:
                print("")
                break
    try:
        key = load_key()
        encrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(mem_key) + "dot" + str(log_key) + ".lg",
                key)
    except:
        pass
    return ct


def delete_line(original_file, line_number):
    say = 0
    key = load_key()
    decrypt(original_file, key)
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    with open(original_file, 'rb') as read_obj, open(dummy_file, 'wb') as write_obj:
        for line in read_obj:
            if current_index != line_number:
                write_obj.write(line)

                say = say+1
            else:

                is_skipped = True
            current_index += 1
    if say == 2:
        os.remove(dummy_file)
        os.remove(original_file)
        return 27
    elif is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
        key = load_key()
        encrypt(original_file, key)
    else:
        os.remove(dummy_file)
        key = load_key()
        encrypt(original_file, key)
    return 0


def dellog(mem_key, log_key,):
    while 1:
        os.system('cls')
        ct = display(mem_key, log_key)
        print("\nEnter the index of the log that is to be deleted, 'n' to go back")
        try:
            i = int(input("-->"))
        except:
            os.system('cls')
            return
        if (i >= ct or i <= 0):
            print("Wrong choice, please try again!\n")
            continue
        else:
            try:
                key = load_key()
                decrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                        str(mem_key) + "dot" + str(log_key) + ".lg", key)
            except:
                pass
            with open("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(mem_key) + "dot" + str(log_key) + ".lg", "rb") as f:
                c = 0
                while 1:
                    try:
                        pickle.load(f)
                        c = c + 1
                        if c == i:
                            dell = {}
                            dell = pickle.load(f)
                            break
                    except EOFError:
                        print("")
                        break
            try:
                key = load_key()
                encrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                        str(mem_key) + "dot" + str(log_key) + ".lg", key)
            except:
                pass
            os.system('cls')
            print("Selected log:", (i), ":", dell, "\n")
            inch = input("To delete enter 'y' or 'n' to go back: ")
            if inch != ('y' or 'Y'):
                break
            else:
                suk = delete_line("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(
                    mem_key) + "dot" + str(log_key) + ".lg", i)
                if suk == 27:
                    os.system('cls')
                    print(users[mem_key] + "'s" + " entire log of " +
                          logs[log_key] + " successfully deleted!\n")
                    return
                os.system('cls')
                print("Successfully deleted!")
                exc = input("\nEnter 'y' to delete more, 'n' to go back: ")
                if exc != ('y' or 'Y'):

                    return
                else:

                    continue


def write_key():

    key = Fernet.generate_key()
    with open("C:\\Users\\Public\\Documents\\Logged Database\\crypto.keylg", "wb") as key_file:
        key_file.write(key)


def set_pass():
    while 1:
        pass1 = input("\nSet Password    : ")
        zeb = len(pass1)
        if zeb < 6:
            os.system('cls')
            print("\n Password must at least 6 characters, please try again!")
            continue
        pass2 = input("\nConfirm Password: ")
        if (pass1 == pass2):
            try:
                key = load_key()
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
            except:
                pass
            with open("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", "wb") as f:
                pickle.dump(pass1, f)
            os.system('cls')
            print("\nNew password created successfully!")
            f.close()
            try:
                key = load_key()
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
            except:
                pass
            break
        else:
            os.system('cls')
            print("\n'Set password' and 'Confirm password' must match, please try again!")
            continue
    return


def load_key():

    return open("C:\\Users\\Public\\Documents\\Logged Database\\crypto.keylg", "rb").read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def getdate():
    return time.asctime(time.localtime(time.time()))


def addmem(ch_t, stri):
    os.system('cls')
    if not ch_t:
        print("\t\t\t\t\tWelcome to Logged!\n")
        print("\t\t\t\t\tAuthor: ady\n")
        if stri == "user":
            print("User database empty!\n")
            print("Add a user to continue!\n")

        else:
            print("Log database empty!\n")
            print("Add a log type to continue!\n")
    if ch_t:
        os.system('cls')
        print("Adding new", stri, "!\n")
    while True:
        count = 1
        con = 1
        for ditckeys in ch_t:
            count += 1
        if ch_t:
            print("Enter new", stri, "or '0' to return to Main Menu ")
        else:
            print("Enter new", stri, "or '0' to exit ")
        mem = input("--> ")
        try:
            con = int(mem)
        except:
            pass
        if con == 0:
            if ch_t:
                return
            else:
                sys.exit("EXIT")
        if stri == "user":
            mem = mem.capitalize()
        for dickeys, values in ch_t.items():
            if mem == values:
                os.system('cls')
                print("There is already a", stri,
                      "named", mem, ",please try again!")
                continue
            else:
                pass
        if stri == "user":
            users[count] = mem
        else:
            logs[count] = mem
        print("\n", stri, " added successfully!\n")
        if stri == "user":
            try:
                key = load_key()
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg.datlg", key)
            except:
                pass
            with open("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", "wb") as f:
                pickle.dump(users, f)
            key = load_key()
            encrypt("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", key)
        else:
            try:
                key = load_key()
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
            except:
                pass
            with open("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", "wb") as f:
                pickle.dump(logs, f)
            key = load_key()
            encrypt("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
        choice = input("Enter 'y' to add more, 'n' to return to Main Menu: ")
        if choice != ('y' or 'Y'):
            os.system('cls')
            return
        else:
            os.system('cls')
            continue


def delmem(ch_t, stri):

    while True:
        cnt = 0
        os.system('cls')
        print("Removing", stri, "!\n")
        global users
        global logs
        for dickey, value in ch_t.items():
            cnt = cnt+1

            print("Enter", dickey, "to remove", value)
        print("Enter '0' to return to Main Menu")
        try:
            mem = int(input("--> "))
        except ValueError:
            os.system('cls')
            print("Invalid input, please try again!\n")
            continue
        if mem == 0:
            os.system('cls')
            return
        if mem not in ch_t:
            os.system('cls')
            print("Wrong choice, please try again!\n")
            continue
        print("\n", stri, ch_t[mem], "removed successfully!\n")
        if stri == "user":

            for dickey2 in logs:
                if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\Logged" + str(mem) + "dot" + str(dickey2) + ".lg"):
                    os.remove("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                              str(mem) + "dot" + str(dickey2) + ".lg")
        else:
            for dictkey in users:
                if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(dictkey)+"dot"+str(mem)+".lg"):
                    os.remove("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                              str(dictkey)+"dot"+str(mem)+".lg")
        if stri == "user":
            del users[mem]

            if users:
                temp = {}
                count = 0
                for items in users:
                    count += 1
                    temp[count] = users[items]
                users = temp
                ch_t = users
                try:
                    key = load_key()
                    decrypt(
                        "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", key)
                except:
                    pass

                with open("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", "wb") as f:
                    pickle.dump(users, f)
                key = load_key()
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", key)
            else:
                if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg"):
                    os.remove(
                        "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg")

                return
        else:
            del logs[mem]
            if logs:
                temp = {}
                count = 0
                for items in logs:
                    count += 1
                    temp[count] = logs[items]
                logs = temp
                ch_t = logs
                try:
                    key = load_key()
                    decrypt(
                        "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
                except:
                    pass

                with open("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", "wb") as f:
                    pickle.dump(users, f)
                key = load_key()
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
            else:
                if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg"):
                    os.remove(
                        "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg")

                return
        if ch_t:
            choice = input(
                "Enter 'y' to remove more, 'n' to return to Main Menu: ")
            if choice != ('y' or 'Y'):
                os.system('cls')
                return
            else:
                os.system('cls')
                continue
        else:
            return


def log():
    while True:
        print("Logging data!\n")
        for dickey, value in users.items():
            print("Enter", dickey, "for", value)
        print("Enter '0' to return to Main Menu")
        try:
            mem_key = int(input("--> "))
        except ValueError:
            os.system('cls')
            print("Invalid input, please try again!\n")
            continue
        if mem_key == 0:
            os.system('cls')
            return

        elif mem_key not in users:
            os.system('cls')
            print("Wrong choice, please try again!\n")
            continue
        while True:
            os.system('cls')
            print("Selected user:", users[mem_key], "\n")
            for dickey, value in logs.items():
                print("Enter", dickey, "to log", value)
            print("Enter '0' to go back")
            try:
                log_key = int(input("--> "))
            except ValueError:
                os.system('cls')
                print("Invalid input, please try again!\n")
                continue
            if log_key == 0:
                os.system('cls')
                break
            elif log_key not in logs:
                os.system('cls')
                print("Wrong choice, please try again!\n")
                continue
            else:
                while (True):
                    os.system('cls')

                    print("Enter", logs[log_key], "for", users[mem_key])
                    text = input("--> ")
                    text = text.capitalize()
                    try:
                        key = load_key()
                        decrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                                str(mem_key)+"dot"+str(log_key)+".lg", key)
                    except:
                        pass
                    if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(mem_key)+"dot"+str(log_key)+".lg"):
                        pass
                    else:
                        with open("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(mem_key)+"dot"+str(log_key)+".lg", "wb") as f:
                            pickle.dump("\n", f)
                    with open("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(mem_key)+"dot"+str(log_key)+".lg", "ab") as f:
                        pickle.dump(str(getdate())+" "+text+"\n", f)
                    key = load_key()
                    encrypt("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                            str(mem_key)+"dot"+str(log_key)+".lg", key)
                    print("\n", users[mem_key], "'s",
                          logs[log_key], "recorded!\n")
                    if len(logs) > 1:
                        choice = input(
                            "Enter 'y' to log more "+logs[log_key]+" for "+users[mem_key]+", 'n' to go back, '0' for Main Menu: ")
                        if choice == '0':
                            return
                        if choice != ('y' or 'Y'):
                            break
                        else:
                            continue
                    else:
                        choice = input("Enter 'y' to log more " + logs[log_key] + " for " + users[
                            mem_key] + ", '0' for Main Menu: ")
                        if choice != ('y' or 'Y'):
                            os.system('cls')
                            return
                        else:
                            continue
                os.system('cls')
                if len(users) > 1:
                    choice = input("Enter 'y' to log more data"+" for " +
                                   users[mem_key] + ", 'n' to log data for other users, '0' to return to Main Menu: ")
                    if choice == '0':
                        return
                    if choice != ('y' or 'Y'):
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        continue
                else:
                    continue
        continue


def retrieve():
    while True:
        print("Retrieving Data!\n")
        for key, value in users.items():
            print("Enter", key, "for", value)
        print("Enter '0' to return to Main Menu")
        try:
            mem_key = int(input("--> "))
        except ValueError:
            os.system('cls')
            print("Invalid input, please try again!\n")
            continue
        if mem_key == 0:
            os.system('cls')
            return
        elif mem_key not in users:
            os.system('cls')
            print("Wrong choice, please try again!\n")
            continue
        os.system('cls')
        while True:
            print("Selected user:", users[mem_key], "\n")
            for dickey, value in logs.items():
                print("Enter", dickey, "to retrieve", value)
            print("Enter 'n' to go back, '0' to return to Main Menu")
            try:
                log_key = int(input("--> "))
            except ValueError:
                os.system('cls')
                break
            if log_key == 0:
                os.system('cls')
                return
            elif log_key not in logs:
                os.system('cls')
                print("Wrong choice, please try again!\n")
                continue
            if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(mem_key)+"dot"+str(log_key)+".lg"):
                ct = display(mem_key, log_key)
                if (len(logs) > 1 or len(users) > 1):
                    print("Enter:\n 'd' to delete specific logs\n 'e' to delete entire " + logs[
                        log_key] + " log for " + users[
                        mem_key] + ",\n 'n' to go back,\n '0' to return to Main Menu")

                else:
                    print("Enter:\n 'd' to delete specific logs\n 'e' to delete entire " + logs[
                        log_key] + " log for " + users[
                        mem_key] + "\n '0' to return to Main Menu")
                choice = input("--> ")
                if choice == '0':
                    os.system('cls')
                    return

                elif choice == ('d' or 'D'):
                    dellog(mem_key, log_key)
                    break
                elif choice == ('e' or 'E'):
                    os.system('cls')
                    exc = input("Enter 'y' to confirm deletion of " +
                                users[mem_key]+"'s"+" entire log of "+logs[log_key]+", or 'n' to go back: ")
                    if exc != ('y' or 'Y'):
                        os.system('cls')
                        continue

                    elif os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\Logged"+str(mem_key)+"dot"+str(log_key)+".lg"):
                        os.remove("C:\\Users\\Public\\Documents\\Logged Database\\Logged" +
                                  str(mem_key)+"dot"+str(log_key)+".lg")
                        os.system('cls')

                        print(users[mem_key]+"'s"+" entire log of " +
                              logs[log_key]+" successfully deleted!\n")
                        break
                elif choice == ('n' or 'N'):
                    os.system('cls')
                    continue

            else:
                os.system('cls')
                print("There are no logs for",
                      users[mem_key], "'s", logs[log_key], "!\n")
                break
        continue


def wel():
    global pp
    key = load_key()
    decrypt("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
    with open("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", "rb") as f:
        pp = pickle.load(f)
    key = load_key()
    encrypt("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
    while (1):
        p = input("Password: ")
        if p == pp:
            os.system('cls')
            break
        else:
            while 1:
                os.system('cls')
                print("Incorrect password!\n")
                print("Enter:\n '1' to try again\n '0' to exit\n 'r' to reset data ")
                i = input("-->")
                if i == '1':
                    os.system('cls')
                    break
                elif i == '0':
                    sys.exit("EXIT")
                elif i == 'r':
                    os.system('cls')
                    print("Enter 'y' to confirm database reset, 'n' to go back")
                    df2 = input("--> ")
                    if df2 == ('y' or 'Y'):
                        dres()
                        os.system('cls')
                        print("Database reset successful!\n")
                        return 16
                    else:
                        os.system('cls')
                        break
    return 0


def main():
    global users, logs

    while (1):
        key = load_key()
        if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg"):
            try:
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", key)
                try:
                    with open("C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", "rb") as f:
                        while 1:
                            try:
                                users = pickle.load(f)
                            except EOFError:
                                break
                except:
                    pass
            except:
                pass
            try:
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\users.datlg", key)
            except:
                pass
        if os.path.exists("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg"):
            try:
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
                try:
                    with open("C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", "rb") as f:
                        while 1:
                            try:
                                logs = pickle.load(f)
                            except EOFError:
                                break
                except:
                    pass
            except:
                pass
            try:
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\logs.datlg", key)
            except:
                pass
        if not users:
            addmem(users, "user")
        if not logs:
            addmem(logs, "log type")
        print("\t\t\t\t\tLogged in Logged!\n")
        print("\t\t\t\t\tAuthor: ady\n")
        print(
            "Main Menu\n\nEnter:\n '1' to log data\n '2' to retrieve/delete data\n '3' to add users\n '4' to add log types\n"
            " '5' remove users/log types/reset database\n '6' to change password\n '0' to exit")
        try:
            z = int(input("--> "))
        except ValueError:
            os.system('cls')
            print("Invalid input, please try again!\n")
            continue
        if z == 1:
            os.system('cls')
            log()
        elif z == 2:
            os.system('cls')
            retrieve()
        elif z == 3:
            os.system('cls')
            addmem(users, "user")
        elif z == 4:
            os.system('cls')
            addmem(logs, "log type")
        elif z == 5:
            os.system('cls')
            #delmem(users, "user")
            while 1:
                print(
                    "Enter:\n '1' to remove user\n '2' to remove log type\n '3' to reset database\n '0' to return to Main Menu")
                try:
                    ef = int(input())
                    pass
                except:
                    os.system('cls')
                    print("Invalid input, please try again!\n")
                    continue
                if ef == 0:
                    break
                if ef == 1:
                    delmem(users, "user")
                    break
                elif ef == 2:
                    delmem(logs, "log type")
                    break
                elif ef == 3:
                    os.system('cls')
                    print("Enter 'y' to confirm database reset, 'n' to go back")
                    df = input("--> ")
                    if df == ('y' or 'Y'):
                        dres()
                        os.system('cls')
                        print("Database reset successful!\n")
                        start()
                        break
                    else:
                        break
                else:
                    os.system('cls')
                    print("Wrong choice, please try again!\n")
                    continue
        elif z == 6:
            os.system('cls')
            while 1:
                pp = ""
                key = load_key()
                decrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
                with open("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", "rb") as f:
                    pp = pickle.load(f)
                key = load_key()
                encrypt(
                    "C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
                print("Enter '0' to return to main menu")
                pass3 = input("\nEnter current password: ")
                if pass3 == 0:
                    break
                if pass3 == pp:
                    os.system('cls')
                    set_pass()
                    break
                else:
                    os.system('cls')
                    print("Incorrect password, try again!\n")
                    continue
        elif z == 0:
            os.system('cls')
            sys.exit("EXIT")
        else:
            os.system('cls')
            print("Wrong choice, please try again!\n")
        continue


def start():
    while 1:
        try:
            os.mkdir("C:\\Users\\Public\\Documents\\Logged Database")
        except FileExistsError:
            pass
        try:
            key = load_key()
            decrypt("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
            key = load_key()
            encrypt("C:\\Users\\Public\\Documents\\Logged Database\\pass.datlg", key)
            t = wel()
            if t == 16:
                continue
            else:
                break
        except:
            dres()
            os.mkdir("C:\\Users\\Public\\Documents\\Logged Database")
            print("\t\t\t\t\tLogged in Logged!\n")
            print("\t\t\t\t\tAuthor: ady\n")
            print("\nHere's to new beginnings!")
            print("\nLet's start by setting up a password for database!")
            write_key()
            set_pass()
            break


users = {}
logs = {}
start()
main()
