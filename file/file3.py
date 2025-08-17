lines_data = ['Amar','Raju','Ravi','Sita','Gita']
with open('file/write.txt', 'w') as f:
    # f.write('This is a new file created for writing.\n')
    # f.write('We can write multiple lines into this file.\n')
    # f.write('File handling in Python is easy and efficient.\n')
          f.writelines(lines_data)

