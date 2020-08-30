import math

def main():
	ciphertext=raw_input("Enter a message : ")
	
	key=int(raw_input("Enter a key: "))

	plaintext=decrypt(key, ciphertext)
	
	print(plaintext)


def decrypt(key, message):
	no_of_columns=int(math.ceil(len(message)/float(key)))
	no_of_rows=key
	no_of_shaded_box=no_of_rows*no_of_columns-len(message)

	plaintext=['']*no_of_columns
	column=0
	row=0

	for symbol in message:
		plaintext[column]+=symbol
		column+=1
		if ((column == no_of_columns) or 
			(column == no_of_columns - 1 and row >= no_of_rows - no_of_shaded_box)):
			column=0
			row+=1

	return ''.join(plaintext)


if __name__=="__main__":
	main()