from datetime import date

capitals = {'Andhra Pradesh':'Amravati or Hyderabad',
'Arunachal Pradesh':'Itanagar',
'Assam':'Dispur',
'Bihar': 'Patna',
'Chhatisgarh':'Naya Raipur',
'Goa': 'Panaji',
'Gujarat': 'Gandhi Nagar',
'Haryana' : 'Chandigarh',
'Himachal Pradesh' : 'Shimla (Summer)/ Dharamshala (Winter)',
'Jharkhand' : 'Ranchi',
'Karnataka' : 'Bengaluru',
'Kerala': 'Thiruvananthapuram',
'Madhya Pradesh' : 'Bhopal',
'Maharashtra' : 'Mumbai',
'Manipur': 'Imphal',
'Meghalaya': 'Shillong',
'Mizoram': 'Aizawal',
'Nagaland': 'Kohima',
'Odisha' : 'Bhubaneshwar',
'Punjab': 'Chandigarh',
'Rajasthan' : 'Jaipur',
'Sikkim' : 'Gangtok',
'Tamil Nadu': 'Chennai',
'Telangana' : 'Hyderabad',
'Tripura': 'Agartala',
'Uttarakhand' : 'Gairsain (Summer)/Dehradun (Winter)',
'Uttar Pradesh' : 'Lucknow',
'West Bengal': 'Kolkata'}

states = capitals.keys()

for setNumber in range(5):
    quizFile = open("QuizSet%s.txt"%(setNumber + 1),'w')
    quizFile.write('Name:\n\nDate:' + str(date.today()) + '\n\nPeriod:')
    quizFile.write('\n\n' + ' ' * 20 + 'Set %s'%(setNumber+1))
    quizFile.close()

    quizAnsFile = open("QuizAnswers%s.txt"%(setNumber + 1),'w')
    quizAnsFile.write("Answer key for set %s"%(setNumber+1))
    quizAnsFile.close()