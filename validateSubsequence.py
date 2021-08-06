# O(n) time \ O(1) space
def validateSubsequence(array,sequence):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
        seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)         




print(validateSubsequence([5,1,22,25,6,-1,8,10,11,17], [1,6,-1,10]))
