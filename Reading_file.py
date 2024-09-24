Nafiz_file = open("Nafiz.txt", "r")
# r=read
# w=Write(return the only value that is last add)
# r+=Read and write
# a=pen(append information onto to the end of the file you can't change the information but you can add information on the file )
for nafiz in Nafiz_file.readlines([1]):
    print(nafiz)
Nafiz_file.close()
# readable works like return bool value
# read works on return the txt file value
# readline work on return 1 line
# readlins work return multipule line of the file
