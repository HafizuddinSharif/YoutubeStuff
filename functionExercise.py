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

words1 = ["what", "hrllo", "sharif", "happy"]
words2 = ["heyy", "cempedak", "guli", "gasing"]









def oddSum(numbers) :

  total = 0

  for number in numbers :
    if (number % 2 == 0) :
      total = total + number

  return total

numbers1 = [1, 2, 3, 4]
numbers2 = [2, 45, 66, 36]










def combinationLock(numberOfDigits, startLock, endLock) :

  count = 0

  for x in range(numberOfDigits) :
    if (startLock[x] > endLock[x]) :
      count = count + (startLock[x] - endLock[x])
    else :
      count = count + (endLock[x] - startLock[x])
    
  return count

numberOfDigits = 5
startLock = [1, 2, 3, 7, 5]
endLock = [2, 3, 4, 5, 6]

print(combinationLock(numberOfDigits, startLock, endLock))
