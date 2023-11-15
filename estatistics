def zoo_statistics():
  
  count_less_than_2 = 0
  count_between_2_and_5 = 0
  count_between_5_and_10 = 0
  count_greater_than_10 = 0

  while True:
      
      response = input("Is there another animal to be recorded? (yes/no): ").lower()

      if response != 'yes':
          break  

      
      age = float(input("Enter the age of the animal: "))

     
      if age < 2:
          count_less_than_2 += 1
      elif 2 <= age < 5:
          count_between_2_and_5 += 1
      elif 5 <= age < 10:
          count_between_5_and_10 += 1
      else:
          count_greater_than_10 += 1


  total_animals = count_less_than_2 + count_between_2_and_5 + count_between_5_and_10 + count_greater_than_10

  if total_animals > 0:
      percent_less_than_2 = (count_less_than_2 / total_animals) * 100
      percent_between_2_and_5 = (count_between_2_and_5 / total_animals) * 100
      percent_between_5_and_10 = (count_between_5_and_10 / total_animals) * 100
      percent_greater_than_10 = (count_greater_than_10 / total_animals) * 100

      print("\nZoo Statistics:")
      print(f"Less than 2 years: {count_less_than_2} animals, {percent_less_than_2:.2f}%")
      print(f"Between 2 and 5 years: {count_between_2_and_5} animals, {percent_between_2_and_5:.2f}%")
      print(f"Between 5 and 10 years: {count_between_5_and_10} animals, {percent_between_5_and_10:.2f}%")
      print(f"Greater than or equal to 10 years: {count_greater_than_10} animals, {percent_greater_than_10:.2f}%")
  else:
      print("No animals recorded.")


zoo_statistics()
