# dictionary example
marks ={'Omprakash':98,'Prakash':99, 'Raushan':100,'Umang':99,'Vivek':99, 56:89}
print(marks)
marks['Raj']=90
for key in marks:
  print(key, ":", marks[key])

marks['Omprakash'] = 100 
print("Updated Marks:", marks)