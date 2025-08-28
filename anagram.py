def isAnagram(st1,st2):
  return sorted(st1) ,sorted(st2)
if __name__=="__main__":
  st1=input()
  st2=input()
  sort1=sorted(st1)
  sort2=sorted(st2)
  if sort1==sort2:
    print("Anagram")
  else:
    print("Not anagram")
  res=isAnagram(st1,st2)
  print(res)
