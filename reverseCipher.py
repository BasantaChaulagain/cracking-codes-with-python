def main():
	message=raw_input("Enter a message: \n")
	translated=""

	i=len(message)

	while i>0:
		translated=translated+message[i-1]
		i=i-1

	print(translated)


if __name__=="__main__":
	main()
