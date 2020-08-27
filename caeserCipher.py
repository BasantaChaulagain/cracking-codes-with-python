def main():
	symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
	length=len(symbols)

	message=raw_input("Enter a string:\n")
	translated=""
	mode=raw_input("Press 'e' for encrypting and 'd' for decrypting: ")
	key=int(raw_input("Enter the key value: "))

	for letter in message:
		if letter in symbols:
			letterIndex=symbols.find(letter)

			if mode=='e':
				translated=translated+symbols[(letterIndex+key)%length]
			elif mode=='d':
				translated=translated+symbols[(letterIndex-key)%length]

	print(translated)


if __name__=="__main__":
	main()