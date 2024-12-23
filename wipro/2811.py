def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


import re
def regexQues():

    text1 = "Hello, World!"
    pattern1 = r"Hello"
    match = re.match(pattern1, text1)
    if match:
        print(f"Match found: {match.group()}")

    text2 = "Welcome to Hellop World!"
    pattern2 = r"World"
    search = re.search(pattern2, text2)
    if search:
        print(f"Search found: {search.group()} at position {search.start()}")

    text3 = "Ram and shyam and ravana."
    pattern3 = r"an"
    matches = re.findall(pattern3, text3)
    print(f"All matches: {matches}")

    text4 = "World is fun"
    pattern4 = r"World"
    for match in re.finditer(pattern4, text4):
        print(f"Match '{match.group()}' found at position {match.start()}")

    text5 = "apple,banana;orange|grape"
    pattern5 = r"[,;|]"
    split_result = re.split(pattern5, text5)
    print(f"Split result: {split_result}")

    text6 = "I have 2 gray and 3 yellow balls."
    pattern6 = r"\d"
    replaced = re.sub(pattern6, "21", text6)
    print(f"Sub result: {replaced}")

    replaced, count = re.subn(pattern6, "no", text6)
    print(f"Replaced text: {replaced}, Substitutions made: {count}")

    pattern7 = re.compile(r"\d{3}-\d{2}-\d{4}")
    text7 = "My SSN is 123-45-6789."
    match = pattern7.search(text7)
    if match:
        print(f"Found: {match.group()}")

    text8 = "My phone number is 123-456-7890."
    pattern8 = r"(\d{3})-(\d{3})-(\d{4})"
    match = re.search(pattern8, text8)
    if match:
        print(f"Full Match: {match.group()}")
        print(f"Area Code: {match.group(1)}")
        print(f"Local Code: {match.group(2)}")
        print(f"Line Number: {match.group(3)}")

    # 10. Using Flags - Example with re.IGNORECASE
    text9 = "Python is amazing. python is fun."
    pattern9 = r"python"
    matches = re.findall(pattern9, text9, re.IGNORECASE)
    print(f"Matches with flag: {matches}")  # Output: ['Python', 'python']


    text10 = "My phone number is 123-456-7890."
    pattern10 = r"(\d{3})"
    match = re.split(pattern10, text10)
    print(match)
# regexQues()




def q1(string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, string))

def q2(string):
    pattern = r'^a(b*)$'
    return bool(re.match(pattern, string))

def q3(string):
    pattern = r'^a(b+)$'
    return bool(re.match(pattern, string))

def q4(string):
    pattern = r'^a(b?)$'
    return bool(re.match(pattern, string))

def q5(string):
    pattern = r'^a(b{3})$'
    return bool(re.match(pattern, string))

def q6(string):
    pattern = r'^a(b{2,3})$'
    return bool(re.match(pattern, string))

def q7(string):
    pattern = r'[a-z]+_[a-z]+'
    return bool(re.search(pattern, string))

def q8(string):
    pattern = r'[A-Z][a-z]+'
    return bool(re.search(pattern, string))

def q9(string):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, string))

def q10(string):
    pattern = r'^\w+'
    return bool(re.match(pattern, string))


# print(q1("abc123"))
# print(q2("abbb"))
# print(q3("abbb"))
# print(q4("ab"))
# print(q5("abbb"))
# print(q6("abb"))
# print(q7("abcdef_"))
# print(q8("abc"))
# print(q9("axyb3"))
# print(q10("!Hello world!"))


"""
Binary Tree Inorder Traversal
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val

        self.left = left

        self.right = right
class Solution:

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        def traverse(node):
            if node:
                # Traverse the left subtree

                traverse(node.left)

                # Visit the current node

                result.append(node.val)

                # Traverse the right subtree

                traverse(node.right)

        traverse(root)

        return result


import re


def w1():
    match = re.match(r"Hello", "Hello, World!")
    print(f"Match found: {match.group()}")



def w2():
    search = re.search(r"Python", "Welcome to Python programming!")
    print(f"Search found: {search.group()} at position {search.start()}")


def w3():
    matches = re.findall(r"in", "The rain in Spain falls mainly in the plain.")
    print(f"All matches: {matches}")


def w4():
    matches = re.finditer( r"Python", "Python is fun. Learning Python is easy.")
    for match in matches:
        print(f"Match '{match.group()}' found at position {match.start()}")


def w5():
    """Split a string by the pattern."""
    split_result = re.split(r"[,;|]", "apple,banana;orange|grape")
    print(f"Split result: {split_result}")


def w6():
    """Substitute a pattern with a string."""

    replaced = re.sub(r"\d", "#", "I have 2 cats and 3 dogs.")
    print(f"Sub result: {replaced}")


def w7():
    """Substitute a pattern and return count of replacements."""
    replaced, count = re.subn( r"\d", "#", "I have 2 cats and 3 dogs.")
    print(f"Replaced text: {replaced}, Substitutions made: {count}")


def w8():
    """Compile a regex pattern for reuse."""
    pattern = re.compile(r"\d{3}-\d{2}-\d{4}")
    text = "My SSN is 123-45-6789."
    match = pattern.search(text)
    if match:
        print(f"Found: {match.group()}")


def w9():
    """Use groups to extract parts of a match."""
    text = "My phone number is 123-456-7890."
    pattern = r"(\d{3})-(\d{3})-(\d{4})"
    match = re.search(pattern, text)
    if match:
        print(f"Full Match: {match.group()}")
        print(f"Area Code: {match.group(1)}")
        print(f"Local Code: {match.group(2)}")
        print(f"Line Number: {match.group(3)}")


def w10():
    """Use flags to modify regex behavior."""
    matches = re.findall(r"python", "Python is amazing. python is fun.", re.IGNORECASE)
    print(f"Matches with flag: {matches}")


