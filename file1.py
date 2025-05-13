text= input("Enter the text:\n")
spam=False

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
 spam=True
elif("subscribe" in text):
 spam=True
elif("click this" in text):
 spam=True
elif("make money" in text):
 spam=True
elif("earn money" in text):
 spam=True
elif("get free" in text):
 spam=True


if(spam):
  print("This text is spam")
else:
  print("THis text is not spam")
