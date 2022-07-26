#TripPlanner V1.0

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

#Calling welcome message
trip_planner_welcome("James")

#Function to calculate rounded time with decimal number
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)


#Destination setup function
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Paris", "Berlin", estimate)
