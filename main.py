import os

PATH = "root"
AB_PATH = os.path.abspath("root")

def abp(path: str): return os.path.abspath(path)

running = True

try:

    while running:

        request = input(f"<{PATH}> % ")
        req_ls = request.split(" ")

        match req_ls[0]:
            case "ls":

                print("    ".join(os.listdir(PATH)))

            case "gt":

                if os.path.exists(abp(PATH + "\\" + req_ls[1])) and req_ls[1] != "..":
                    PATH += "\\" + req_ls[1]
                    AB_PATH = abp(PATH)

                elif req_ls[1] == ".." and PATH != "root":
                    PATH = PATH[0 : PATH.rfind("\\")]

                elif req_ls[1] == ".." and PATH == "root":
                    print("Can't go beyond root directory")

                elif not os.path.exists(abp(PATH + "\\" + req_ls[1])):
                    print("Directory does not exist")

            case "mkdir":

                if not os.path.exists(abp(PATH + "\\" + req_ls[1])):
                    os.mkdir(AB_PATH + "\\" + req_ls[1])

                elif os.path.exists(abp(PATH + "\\" + req_ls[1])):
                    print("This directory already exists")

            case "del":
                try:
                    if os.path.exists(abp(PATH + "\\" + req_ls[1])):
                        os.remove(AB_PATH + "\\" + req_ls[1])

                    if not os.path.exists(abp(PATH + "\\" + req_ls[1])):
                        print("This object does not exist")
                except PermissionError as err:
                    print("Cannot delete file")
                    print(err)

            case "quit":
                running = False
                break

except KeyboardInterrupt:
    pass


