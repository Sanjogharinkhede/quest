# Leetcode Copy  Mostly Questions are  from leetcode so solved there to get better testcases
# Copied here
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


def exceptionHandling():
    try:
        numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

        index = int(input("Enter index : "))
        value = numbers[index]

        new_value = int(input("value to update at the index: "))
        numbers[index] = new_value
    except IndexError:
        print("Index out of range")
    except ValueError:
        print("Please enter a valid Int number.")
    else:
        print(f"Updated list: {numbers}")
    finally:
        print("executed.")



a = 5
def q(**i):
    global a
    print(a)
    print(i)


# q(g="d",b="d")


def maxArea(height):
    """
    Leetcode
    11. Container With Most Water
    :param self:
    :param height:
    :return:
    """
    a, b = 0, len(height) - 1
    maxArea = 0

    while (a < b):
        area = 0
        if (height[a] > height[b]):
            area = (b - a) * (height[b])
            b -= 1
        else:
            area = (b - a) * (height[a])
            a += 1

        if (area > maxArea):
            print(a, b)
            maxArea = area

    return maxArea


def findSubstring(s: str, words):
    """
    Leetcode
    30. Substring with Concatenation of All Words

    :param self:
    :param s:
    :param words:
    :return:
    """

    from collections import Counter
    if not s or not words:
        return []

    wordsLen = len(words)
    eachWordLen = len(words[0])
    totalWordsLen = eachWordLen * wordsLen
    wordCounterMap = Counter(words)
    # print(wordsLen,eachWord,totalWordsLen,wordMap)
    stringLen = len(s)
    ans = []
    i = 0
    while (i + totalWordsLen) <= stringLen:
        st = s[i: i + totalWordsLen]
        j = 0
        countersMap = Counter()

        while j < len(st):
            string = st[j: j + eachWordLen]
            j += eachWordLen
            if string not in wordCounterMap:
                break
            else:
                countersMap[string] += 1
        # print(countersMap,wordCounterMap)
        if countersMap == wordCounterMap:
            ans.append(i)
        i += 1
    return ans


def findMedianSortedArrays(nums1, nums2):
    """
    4. Median of Two Sorted Arrays
    :param nums1:
    :param nums2:
    :return:
    """
    lst = []
    l1, l2 = len(nums1), len(nums2)

    l = l1 + l2

    if (l1 == 0 and l2 == 1): return nums2[0]
    if (l2 == 0 and l1 == 1): return nums1[0]

    a = b = 0

    while (a < l1 and b < l2):
        if (nums1[a] > nums2[b]):
            lst.append(nums2[b])
            b += 1
        else:
            lst.append(nums1[a])
            a += 1

    if (l1 == a):
        lst += nums2[b:]
    if (l2 == b):
        lst += nums1[a:]

    if (l % 2 != 0):
        return lst[l // 2]
    return (lst[l // 2] + lst[(l // 2) - 1]) / 2


def reverse(x):
    """
    Leetcode
    7. Reverse Integer
    :param x:
    :return:
    """

    def rev(x):
        y = 0
        while x > 0:
            y = (y * 10) + x % 10
            x //= 10
        return y

    y = rev(x) if (x > 0) else -rev(-x)

    return 0 if y <= -(2 ** 31) or y >= (2 ** 31) - 1 else y
