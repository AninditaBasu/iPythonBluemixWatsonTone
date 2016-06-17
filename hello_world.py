#
print "Hello, I am a sample application."
a_name = raw_input("Your name is? ")
print "Hello", a_name
#
f = open ("./static/hello.txt")
for line in f:
    print line
f.close()
#
