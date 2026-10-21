

path = 'test_file.log'
file = open(path,mode='r')
# reading the entire content
content = file.read()
content = content + '\nNOTE:This file was writed by Aymane Galibou'

file2 = open('result.txt',mode='w')
# writing the new content in a separeated new file 
file2.write(content)

# uncomment to show the difference
# file2.close()

file3 = open('result.txt',mode='r')
content3 = file3.read()
print(content3)
print('file wont be read cause file2 not closed')
file.close()

