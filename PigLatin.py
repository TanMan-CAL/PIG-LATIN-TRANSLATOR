# Using Python, I created a Pig Latin translator. 
def main():
  string_input = input("STRING: ")
  string = string_input.split()
  output_string = []
  list = []
  first_letter_list = []

  print("CONVERTING TO PIG LATIN...")
  print("")


  for i in range(len(string)):
    first_letter_list.append(string[i][0])
    string[i] = string[i].lstrip(string[i][0])
    string[i] = string[i].capitalize()
    list.append(string[i])
    


    output_string += list[i]
    output_string += first_letter_list[i]
    output_string += 'AY'
    output_string += ' '



    

  print(output_string.upper())







main()
