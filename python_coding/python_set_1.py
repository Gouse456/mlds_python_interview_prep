# A. Character-Based Problems
# 1. First Non-Repeating Character
# def my_function(value):
#     s = value
#     d = {}
#     for ch in s:
#         if ch in d:
#             d[ch]+=1
#         else:
#             d[ch] = 1
#     for nch in s:
#         if d[nch] == 1:
#             return nch
#             break

# nch_value = my_function("yolo life")
# print(nch_value)

#####################################################################################################

# 2. Most Frequent Character
# s = "yolo life"
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch] = 1

# sort by frequency
#sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# print(sorted_chars)

#printing first most frequent element 
# print(sorted_chars[0][0])

#printing top k frequent elements
# k = 2
# result = []
# for ch, count in sorted_chars[:k]:
#     result.append(ch)
# print(result)


#Top K Frequent Elements 🔥🔥
# nums = [1,1,1,2,2,3]
# k = 2

# freq = {}

# for num in nums:
#     freq[num] = freq.get(num, 0) + 1

# sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# result = []

# for i in range(k):
#     result.append(sorted_nums[i][0])

# print(result)

################################################################################################################

# 2.Remove duplicate characters while keeping order
 
# s = "yoyo life"
# s1 = ""
# for ch in s:
#     if ch not in s1:
#         s1 += ch
# print(s1)

# # Remove Duplicate Characters (Sorted Output)
# print(''.join(sorted(s1)))

#Remove Duplicate Words from Sentence
# sentence = "a dog is dog where it lives"
# words = sentence.split()
# w2 = []
# for w in words:
#     if w not in w2:
#         w2.append(w)
# updated_sen = ' '.join(w2)
# print(updated_sen)

#Check if String Has All Unique Characters
s = "good"
# if len(s) == len(set(s)):
#     print("All Unique Characters")
# else:
#     print("Not All Unique Characters")

#Count Duplicate Characters and Find All Duplicate Characters

# s = "yoyo life"
# d = {}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch] = 1
# print(d)
# print("\n")
# print("Find All Duplicate Characters")
# duplicate_charcaters = {k: v for k, v in d.items() if v > 1}
# print(duplicate_charcaters)
# print("\n")
# print("Counting Duplicate Characters")
# count = len(duplicate_charcaters)
# print(f"there are {count} duplicate characters")

###########################################################################################################

# 3.Check if a String is a Palindrome
# s = "mom"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Checking using two-pointer technique 

# s = "gouse"
# left = count  = 0
# right = len(s)-1
# while(left <= right):
#     if s[left] == s[right]:
#         count+=1
#     else:
#         print("Not a Palindrome")
#         break
#     left+=1
#     right-=1
# if ((len(s)//2) + 1) == count:
#     print("Palindrome")


# Reverse a String without slicing

# s  = "gouse"
# s = list(s)
# l = 0
# r = len(s)-1
# while(l < r):
#     s[l],s[r] = s[r],s[l]
#     l+=1
#     r-=1
# print("".join(s))

# Check if Two Strings are Anagrams

# s = "gouse"
# s1 = "good"

# if sorted(s) == sorted(s1): #using sorted
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# d = {} #using dict
# d1 = {}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch] = 1

# for ch in s1:
#     if ch in d1:
#         d1[ch]+=1
#     else:
#         d1[ch] = 1

# if d == d1:
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# Count Vowels in a String -- frequency
# s = "gouse"
# count = 0
# for i in s:
#     if i.lower() in "aeiou":
#         count+=1
# print(count)

# count = 0   #we want to count unique vowels
# s1 = set(s)
# for i in s1:
#     if i.lower() in "aeiou":
#         count+=1
# print(count)

#############################################################################################################

# # 5 . Reverse each word in a sentence without changing word order
# sen = "you are a dog"
# new_sen = []
# words = sen.split()
# for i in words:
#     new_sen.append(i[::-1])
# new_sen = " ".join(new_sen)
# print(new_sen)

#################################################################################################################

# 6. Convert string to Title Case (without built-in .title())
# sen = "you are a dog"
# new_sen = []
# words = sen.split()
# for ch in words:
#     w = ch[0].upper() + ch[1:]
#     new_sen.append(w)
# print(new_sen)

#################################################################################################################

# 7. Count uppercase and lowercase letters
# sen = "Gouse"
# u_count = l_count = 0
# for i in sen:
#     if i.isupper():
#         u_count+=1
#     if i.islower():
#         l_count+=1
# print(u_count)
# print(l_count)

###################################################################################################################

# 8 . Find the longest word in a sentence
# sen = "you are a dogg"
# d = {}
# words = sen.split()
# for w in words:
#     d[w] = len(w)
# print(d)

# sorted_l = sorted(d.items(),key = lambda x :x[1],reverse=True)
# print(sorted_l[0])

######################################################################################################################

# 9 . Check if a number is Prime

num = 3
if num <= 1:
    print("not prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")



###################################################################################################################
# 10 . Find the largest number in a list

# l = [10,8,5,2,12]
# maxi = l[0]
# for i in range(0,len(l)):
#     if l[i] > maxi:
#         maxi = l[i]
# print(maxi)


# Finding second largest number

l = [1,8,5,2,12]
maxi = sec_max = 0
for i in range(0,len(l)):
    if l[i] > maxi:
        sec_max = maxi
        maxi = l[i]
print(maxi)
print(sec_max)