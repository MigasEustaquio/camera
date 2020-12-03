import facerecognizer

if __name__ == "__main__":
  
	name = facerecognizer.recog()

	if name == "unknown":
		print("\nSecurity Breach\n")
	else:
		print("\n" + name + "\n")
