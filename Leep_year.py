
year = int(input("Which year do you want to check? "))

year = int(year)
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is leep year")
    else: 
      print(f"{year} is not leep year")
  else: 
    print(f"{year} is not leep year")
else: 
  print(f"{year} is not leep year")
