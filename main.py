# coding=utf-8
""""

Plasma OS by Plasm Inc.

"""
import os
import shutil

PATH = "root"
AB_PATH = os.path.abspath("root")


def abp(path: str):
	"""
	Returns absolute path
    :param path:
	:return:
	"""
	try:
		return os.path.abspath(path)
	except:
		print("Path error")
		return None


running = True

try:

	while running:

		request = input(f"<{PATH}> ~ ")
		req_ls = request.split(" ")

		if "/" in request:
			print("Use '\\' instead of '/'")
			continue

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
						PATH = PATH[0: PATH.rfind("\\")]

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
							if os.path.isfile(PATH + "\\" + req_ls[1]):
								os.remove(PATH + "\\" + req_ls[1])
							else:
								shutil.rmtree(PATH + "\\" + req_ls[1])

						elif not os.path.exists(PATH + "\\" + req_ls[1]):
							print("This object does not exist")

					except PermissionError as err:
						print("Cannot delete file")
						print(err)

				case "mv":
					if not os.path.exists(req_ls[1]):
						print("File not found")

					elif os.path.exists(req_ls[2]):
						print("The endpoint already has such a file")

					elif not os.path.exists(req_ls[2][0: req_ls[2].rfind("\\")]):
						print("There is no final path")

					else:
						shutil.move(req_ls[1], req_ls[2])

				case "copy":
					if not os.path.exists(req_ls[1]):
						print("File not found")

					elif os.path.exists(req_ls[2]):
						print("The endpoint already has such a file")

					elif not os.path.exists(req_ls[2][0: req_ls[2].rfind("\\")]):
						print("There is no final path")

					else:
						shutil.copy(req_ls[1], req_ls[2])

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
					print("gt <directory> -> go to the specified directory in the current directory.\n")
					print("mdir <name of directory> -> create a new directory in the current directory.\n")
					print("del <name of object> -> delete object in the current directory (may not work).\n")
					print("mv <path to the object (with root and object)> <path where to move the object (with root and"
					      "name of object)> -> move file from the first directory to the second.\n")
					print("copy <path to the object (with root and object)> <path where to copy the object (with root"
					      "and name of object)> -> copy file from the first directory to the second.\n")
					print("ren <name of object> <new name of object> -> rename file in the current directory.\n")
					print("run <name of file> -> run file in current directory(only .py or .bat files).\n")

				case "quit":
					running = False
					break
		except IndexError:
			print("Invalid syntax")
		except BaseException as err:
			print("Error")
			print("Details:")
			print(err)

		AB_PATH = abp(PATH)

except KeyboardInterrupt:
	pass
