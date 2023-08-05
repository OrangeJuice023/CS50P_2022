# Gets the filename that the user wants
desired_filename = input("File name: ").lower().strip()

# If the following extensions - gif or png or jpg or jpeg, print "image/type"
if desired_filename.endswith(".jpg"):
    print("image/jpeg")
elif ".png" in desired_filename:
    print("image/png")
elif desired_filename.endswith(".gif"):
    print("image/gif")
elif ".jpeg" in desired_filename:
    print("image/jpeg")

# If the following extensions - pdf or , print "application/type"
elif desired_filename.endswith(".pdf"):
    print("application/pdf")
elif ".zip" in desired_filename:
    print("application/zip")

# If txt, print "text/plain"
elif desired_filename.endswith(".txt"):
    print("text/plain")

# Else, print "application/octet-stream"
else:
     print("application/octet-stream")
