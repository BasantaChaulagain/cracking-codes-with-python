def main():
	symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
	length=len(symbols)

	message=raw_input("Enter a string:\n")

	for key in range(length):
		translated=""
		for letter in message:
			if letter in symbols:
				letterIndex=symbols.find(letter)
				translated=translated+symbols[(letterIndex-key)%length]

		print("key #{}: {}".format(key, translated))


if __name__=="__main__":
	main()