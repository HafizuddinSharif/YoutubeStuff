# If word have 'f', 'r', 'm', 's'
def capitalizeWords(words) :
  selectedLetters = "frms"
  answer = []

  for word in words :

    added = False

    for letter in word :

      if letter in selectedLetters :
        answer.append(word.capitalize())
        added = True
        break

    if not added :
      answer.append(word)
  
  return answer

# Answer is ["what", "Hrllo", "Sharif", "happy"]
words1 = ["what", "hrllo", "sharif", "happy"]

# Answer is ["heyy", "Cempedak", "guli", "Gasing"]
words2 = ["heyy", "cempedak", "guli", "gasing"]

print(capitalizeWords(words1))
print(capitalizeWords(words2))


def evenSum(numbers) :
  
  total = 0

  for number in numbers :
    if (number % 2 == 0) :
      total = total + number

  return total


# Answer is 6
numbers1 = [1, 2, 3, 4]

# Answer is 104
numbers2 = [2, 45, 66, 36]

print(evenSum(numbers1))
print(evenSum(numbers2))


def combinationLock(startLock, endLock):
  
  totalCount = 0

  for x in range(5) :
    if (startLock[x] > endLock[x]) :
      spinCount = startLock[x] - endLock[x]
    else :
      spinCount = endLock[x] - startLock[x]

    if spinCount > 5 :
      totalCount = totalCount + (10 - spinCount)
    else :
      totalCount = totalCount + spinCount
    
  return totalCount


# Answer is 7
startLock1 = [1, 2, 3, 4, 5]
endLock1 = [2, 3, 4, 7, 6]

# Answer is 6
startLock2 = [1, 2, 3, 1, 5]
endLock2 = [2, 3, 4, 9, 6]

print(combinationLock(startLock1, endLock1))
print(combinationLock(startLock2, endLock2))
