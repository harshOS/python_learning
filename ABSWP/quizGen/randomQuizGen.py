import  random
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


for setNumber in range(5):
    quizFile = open("QuizSet%s.txt"%(setNumber + 1),'w')
    quizFile.write('Name:\n\nDate:' + str(date.today()) + '\n\nPeriod:')
    quizFile.write('\n\n' + ' ' * 20 + 'Set %s\n'%(setNumber+1))
#    quizFile.close()

    quizAnsFile = open("QuizAnswers%s.txt"%(setNumber + 1),'w')
    quizAnsFile.write("Answer key for set %s\n"%(setNumber+1))
#   quizAnsFile.close()

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(28):

        correctOption = capitals[states[questionNum]]
        wrongOptions = list(capitals.values())
        del wrongOptions[wrongOptions.index(correctOption)]
        wrongOptions = random.sample(wrongOptions,3)

        options = [correctOption] + wrongOptions
        random.shuffle(options)
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        print('written',questionNum)
        for i in range(4):
            quizFile.write('%s.%s\n'%('ABCD'[i],options[i]))
        quizFile.write('\n\n')

        quizAnsFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[options.index(correctOption)]+'. '+correctOption))

    quizAnsFile.close()
    quizFile.close()