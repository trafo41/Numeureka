print('='*100)

with open('Girls names.txt') as file1:
    Lines = file1.readlines()
#                        or 
# path = r'C:\Users\LENOVO\Desktop\python2020\g_names2.txt'
# file1 = open(path, 'r')
# Lines = file1.readlines()
# file1.close()

# l = ['1','2','2','2','5','5','5','5','5','1','1','5','5']
albhabets = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



names_list = []
for line in Lines:
    j =set(line.strip().split())
    names_list.append(j) 

names_dict ={}
for i in range(13,len(names_list)):
    names_dict[i] = names_list[i-1]



def name_score(name):
    nums = []
    for i in name:
        # if i in list1:                                             not needed bcoz that we have already checked earlier
        nums.append(albhabets.index(i))

    print(nums)
    print('-'*len(name)*3 + "------")                                 
    print("Numerical value of your name : ", sum(nums))

    partners_score = 100 - sum(nums)                                # if you want sum other than 100, just replace 100 here by that number

    name_suggestions = names_dict.get(partners_score)
    if name_suggestions:
         print('-'*55 + '\nHere are some names which makes perfect 100 with your name :\n')
         print(*name_suggestions, sep='   |  ')
    else:
        print("Sorry currently we don't have any name for score", partners_score)



g = 'y'
while(g == 'y'):

    word = list(input("\nEnter a word : ").upper())
    print("\n",*word, sep='  ')                                        # *word instead of using join and all

    flag = True
    for i in word:
        if i not in albhabets:
            print("Please use alphabetical characters only, ({}) and other similar characters/digits are not valid".format(i))
            flag = False
            break
    
    if flag == True:
        name_score(word)

    print("\nDo yoy want to continue ? : Y/N")
    z = input()
    if z == 'n' or z == 'N':
        g = 'Stop'                                                     # now g = y not anymore   


# check the Name score / Name numeral of your name  // for eg. Jai : (10 + 1 + 9) = 20  | Aman : (1 + 13 + 1 + 14) = 29
# Check if your and your partner's name together make perfect 100  // Aman + Jasmine : (1 + 13 + 1 + 14) + (10 + 1 + 19 + 13 + 9 + 14 + 5) = 100
# Check what Name numeral your and your partner's name makes together  //  Jai + Aarohi : (10 + 1 + 9) + (1 + 1 + 18 + 15 + 8 + 9) = 72
# Do you want me to suggest some names that make perfect 100 with your name
# Do you want me to suggest me some name for a number 