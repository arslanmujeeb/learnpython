def understanding_main():
	print("i am inside the function")

print(__name__)

'''I am using __name__ == __main__ here because i dont want the understanding_main() to be called when imported only. This way i can only call the understanding_main()
function when i want in the other files when this is imported''' 
if __name__ == "__main__":
	understanding_main()