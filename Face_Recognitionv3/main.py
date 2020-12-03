import facedetect
import facetrain
import facerecognizer
from data import library

if __name__ == "__main__":
	
	#library.initialize() #comentado para teste
	
	x=9
	
	while(1):
		if x==10:
			print("Do you wanna run anything else?")
		x=int(input("Face Detection (1), AI Train (2), Face Recognition (3), Quit (0)\n"))
		
		if x == 1:
			library.led(1)
			facedetect.detect()
			library.led(0)
			y=input("Do you to train the model now?(y/n)")
			if y == "y":
				facetrain.train()
				print("\n")
			x=10
			#break
		elif x == 2:
			facetrain.train()
			print("\n")
			#break
		elif x == 3:
			library.led(1)
			name = facerecognizer.recog()
			library.led(0)
			library.recognized(name)
			print("\n\nbanana\n\n")
		elif x == 0:
			print("Goodbye\n")
			break
	
