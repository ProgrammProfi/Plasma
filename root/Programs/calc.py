while True:
	req = input("Enter an expression. For quit type 'quit' >")
	if req == "quit":
		break
	try:
		print(f"{req} = {eval(req)}")
	except:
		print("Math error!")
