def findNumOfStepsRequired(no_of_patients,steps_of_patient):
  return no_of_patients*steps_of_patient
  
if __name__ == "__main__":
    no_of_patients = int(input('enter the no of patients of escaped'))
    steps_of_patient = int(input('enter the steps of first patient'))
    requiredSteps = findNumOfStepsRequired(no_of_patients,steps_of_patient)
    print(requiredSteps)