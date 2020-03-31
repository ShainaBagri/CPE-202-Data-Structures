# float string -> float
# Given earth weight and planet, returns weight on provided planets
def weight_on_planets(pounds, planet):
   if planet=='Mars':
      return pounds*0.38
   elif planet=='Jupiter':
      return pounds*2.34
   elif planet=='Venus':
      return pounds*0.91
   else:
      raise ValueError

if __name__ == '__main__':
   pounds = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.")