cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print (threes_and_fives)

'''
Our message is backwards.
The letter we want is every other letter.
'''
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]


'''
Create message
Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s.
The second argument will be garbled.

Finally, print your message to the console.'''
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message1 = filter(lambda x: x != 'X', garbled)
print( message )
