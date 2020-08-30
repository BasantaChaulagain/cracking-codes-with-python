def main():
	message=raw_input("Enter a message : ")
	key=int(raw_input("Enter a key: "))

	ciphertext=encrypt(key, message)
	
	print(ciphertext + '|')


def encrypt(key, message):
	ciphertext=['']*key
	for column in range(key):
		currentIndex=column
		while (currentIndex<len(message)):
			ciphertext[column]+=message[currentIndex]
			currentIndex+=key

	return ''.join(ciphertext)


if __name__=="__main__":
	main()