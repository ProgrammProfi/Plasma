import os
import shutil

# import ctypes
# import sys
#
#
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
#
# if is_admin():
#     pass
# else:
#     # Перезапускаем скрипт с правами админа
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     exit()  # выходим из старой версии скрипта


PATH = "root"
AB_PATH = os.path.abspath("root")


def abp(path: str): return os.path.abspath(path)


running = True

try:

    while running:

        request = input(f"<{PATH}> ~ ")
        req_ls = request.split(" ")

        try:
            match req_ls[0]:
                case "ls":

                    print("    ".join(os.listdir(PATH)))

                case "run":

                    if req_ls[1].endswith(".py"):
                        if os.path.exists(PATH + "\\" + req_ls[1]):
                            f = open(PATH + "\\" + req_ls[1])
                            exec(f.read())
                            f.close()
                        else:
                            print("File not found")
                    elif req_ls[1].endswith(".bat"):
                        if os.path.exists(PATH + "\\" + req_ls[1]):
                            os.startfile(f"{PATH}\\{req_ls[1]}")
                        else:
                            print("File not found")
                    else:
                        print("Cannot run this file")

                case "gt":

                    if os.path.exists(PATH + "\\" + req_ls[1]) and req_ls[1] != "..":
                        PATH += "\\" + req_ls[1]

                    elif req_ls[1] == ".." and PATH != "root":
                        PATH = PATH[0 : PATH.rfind("\\")]

                    elif req_ls[1] == ".." and PATH == "root":
                        print("Can't go beyond root directory")

                    elif not os.path.exists(PATH + "\\" + req_ls[1]):
                        print("Directory does not exist")

                case "mdir":

                    if not os.path.exists(PATH + "\\" + req_ls[1]):
                        os.mkdir(PATH + "\\" + req_ls[1])

                    elif os.path.exists(PATH + "\\" + req_ls[1]):
                        print("This directory already exists")

                case "del":
                    try:
                        if os.path.exists(PATH + "\\" + req_ls[1]):
                            os.remove(PATH + "\\" + req_ls[1])

                        elif not os.path.exists(PATH + "\\" + req_ls[1]):
                            print("This object does not exist")

                    except PermissionError as err:
                        print("Cannot delete file")
                        print(err)

                case "mv":
                    if not (os.path.exists(req_ls[1]) and os.path.exists(req_ls[2])):
                        print("Invalid paths")

                    elif os.path.exists(req_ls[1]) and os.path.exists(req_ls[2]):
                        shutil.move(req_ls[1], req_ls[2])

                case "copy":
                    if not os.path.exists(req_ls[1]):
                        print("Invalid path")

                    elif os.path.exists(req_ls[1]) and os.path.exists(req_ls[2]):
                        print("The endpoint already has such a file")

                    elif os.path.exists(req_ls[1]) and not os.path.exists(req_ls[2]):
                        shutil.move(req_ls[1], req_ls[2])

                case "ren":
                    if not os.path.exists(PATH + "\\" + req_ls[1]):
                        print("File not found")

                    elif os.path.exists(PATH + "\\" + req_ls[2]):
                        print("Such a file already exists")

                    else:
                        try:
                            os.rename(PATH + "\\" + req_ls[1], PATH + "\\" + req_ls[2])
                        except PermissionError as err:
                            print("Cannot rename file")
                            print(err)

                case "help":
                    print("ls -> list of all objects in the current directory.\n")
                    print("gt <directory in list> -> go to the specified directory in thr current directory.\n")
                    print("mkdir <name of directory> -> create a new directory in the current directory.\n")
                    print("del <name of object> -> delete object in the current directory (may not work).\n")
                    print("mv <path to the object (with root)> <path where to move the object (with root)> -> move file from the first directory to the second.\n")
                    print("copy <path to the object (with root)> <path where to copy the object (with root)> -> copy file from the first directory to the second.\n")
                    print("ren <name of object> <new name of object> -> rename file in the current directory.\n")
                    print("run <name of file> -> run file in current directory(only .py or .bat files).\n")

                case "quit":
                    running = False
                    break
        except IndexError:
            print("Invalid syntax")

        AB_PATH = abp(PATH)

except KeyboardInterrupt:
    pass
