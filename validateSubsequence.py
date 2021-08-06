# O(n) time \ O(1) space
# def validateSubsequence(array, subsequence):
#   arrIdx = 0
#   seqIdx = 0

#   while arrIdx < len(array) and seqIdx < len(subsequence):
#     if array[arrIdx] == subsequence[seqIdx]:
#       seqIdx += 1
#     arrIdx += 1

#   return seqIdx == len(subsequence)    




def validateSubsequence(array, sequence):
  indexOfSequence = 0

  for value in array:
    if indexOfSequence == len(sequence):
      break
    if sequence[indexOfSequence] == value:
      indexOfSequence += 1
  return indexOfSequence == len(sequence)   



print(validateSubsequence([5,1,22,25,6,-1,8,10,11,17], [1,6,-1,10]))
