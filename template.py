def cypher(x,key):
  #lists for storage and comparison
  sym = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*"]
  num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
  temp = []
  final = []

  #convert symbols into numbers
  for i in range(len(x)):
    for j in range(len(sym)):
      if x[i] == sym[j]:
        temp.append(num[j])
  #change what the number is using the key
  

  #convert back into symbols
  for i in range(len(temp)):
    for j in range(len(num)):
      if temp[i] == num[j]:
        final.append(sym[j])
  print(*final,sep="")


ky = int(input("key(number): "))
txt = input("text: ")
cypher(txt,ky)
