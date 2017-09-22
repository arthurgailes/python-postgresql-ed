age = input('Enter your age: ')


seconds = (int(age)*365*24*60*60)

#using branckets inside print without needing to make it a string
print("You have lived for {} seconds. This corresponds to {} years".format(seconds, age))

