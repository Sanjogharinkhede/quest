# Leetcode Copy
from collections import Counter


def findSubstring(s, words):
    if not s or not words:
        return []

    wordsLen = len(words)
    eachWord = len(words[0])
    totalWordsLen = eachWord * wordsLen

    wordMap = Counter(words)

    # print(wordsLen,eachWord,totalWordsLen,wordMap)

    stringLen = len(s)
    ans = []

    for i in range(eachWord):
        l = i
        r = i
        currentCount = Counter()
        # print(l,r,currentCount)

        while r + eachWord <= stringLen:

            word = s[r:r + eachWord]
            r += eachWord
            # print(word)

            if (word in wordMap):
                currentCount[word] += 1
                print(l, r, currentCount)

                while currentCount[word] > wordMap[word]:
                    currentCount[s[l:l + eachWord]] -= 1
                    l += eachWord

                if r - l == totalWordsLen:
                    ans.append(l)
            else:
                currentCount.clear()
                l = r
    return ans


# print(findSubstring("barfoothefoobarman",["foo","bar"]))
# print(findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))

#
# try:
#     numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
#     index = int(input("Enter index : "))
#     value = numbers[index]
#
#     new_value = int(input("value to update at the index: "))
#     numbers[index] = new_value
# except IndexError:
#     print("Index out of range")
# except ValueError:
#     print("Please enter a valid Int number.")
# else:
#     print(f"Updated list: {numbers}")
# finally:
#     print("executed.")
#
#
a=5
def q(**i):
    global a
    print(a)
    print(i)

q(g="d",b="d")

solution.__doc__()