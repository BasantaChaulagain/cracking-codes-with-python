import random, sys
import transpositionEncrypt, transpositionDecrypt

def main():
	random.seed(41)

	for i in range(10):
		message='ABCDEFGHIJKLMNOPQRSTUVWXYZ'*random.randint(4,40)
		# message='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		message=list(message)
		random.shuffle(message)
		message=''.join(message)

		for key in range(1, len(message)/2):
			# print("original : "+message)
			# print("key : "+str(key))
			encrypted=transpositionEncrypt.encrypt(key, message)
			# print("encrypted : "+encrypted)
			decrypted=transpositionDecrypt.decrypt(key, encrypted)
			# print("decrypted : "+decrypted+"\n")

			if (decrypted!=message):
				print("Mismatch with key {} and message {}.".format(key, message))
				sys.exit()

		print("Test successful.")


if __name__=="__main__":
	main()