with open("file1.txt", "r") as file:
    text = file.read()

   words = text.split()


   count = []


   for word in words:
       if word in count:
           count[word] += 1
       else:
           count[word] = 1

     max_word = ""
     max_count = 0

     for word in count:
         if count[word] > max_count:
             max_count = count[word]
             max_word = word

     print("Word with maximum occurrences:", max_word)
     print("Number of occurrences:", max_count)
             
