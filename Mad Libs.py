name = input("Enter a name: ")
nouns = []
print("Enter nouns: ")
for i in range(0, 6):
    give = input()
    nouns.append(give)

verbs = []
print("Enter verbs: ")
for j in range(0, 9):
    put = input()
    verbs.append(put)

nums = []
print("Enter numbers: ")
for l in range(0, 2):
    num = input()
    nums.append(num)

print("My name is " + name + " and I've known the graduate for")
print(nums[0] + " years. I " + verbs[0] + " all the way from " + nouns[0])
print("to celebrate this day. I can still remember when you were in")
print(nums[1] + " grade. How the time has flown by. My best advice is")
print("\"Be sure to " + verbs[1] + " before you " + verbs[2] + ", but don't")
print("ever " + verbs[3] + " your professor.\" On your first day of " + nouns[1])
print("don't forget to " + verbs[4] + ". Remember, family")
print("will " + verbs[5] + " so also " + verbs[6] + "! On Friday nights don't")
print(verbs[7] + " at least until you have a " + nouns[2] + ".")
print("College is " + verbs[8] + " so you will need " + nouns[3] + ".")
print("I wish you " + nouns[4] + " and " + nouns[5] + " on this new step in life.")
