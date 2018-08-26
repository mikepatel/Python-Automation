#! python3
# randomQuizGenerator.py - create quizzes and answers in random order, along with key

import random

# dictionary of state capitals
stateCapitals = {
	'Alabama': 'Montgomery', 'Alaska': 'Juneau',
	'Arizona': 'Phoenix', 'Arkansas':'Little Rock',
	'California': 'Sacramento', 'Colorado': 'Denver',
	'Connecticut': 'Hartford', 'Delaware': 'Dover',
	'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
	'Hawaii': 'Honolulu', 'Idaho': 'Boise',
	'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
	'Iowa': 'Des Moines', 'Kansas': 'Topeka',
	'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
	'Maine': 'Augusta', 'Maryland': 'Annapolis',
	'Massachusetts': 'Boston', 'Michigan': 'Lansing',
	'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
	'Missouri': 'Jefferson City', 'Montana': 'Helena',
	'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
	'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
	'New Mexico': 'Santa Fe', 'New York': 'Albany',
	'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
	'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
	'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
	'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
	'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
	'Texas': 'Austin', 'Utah': 'Salt Lake City',
	'Vermont': 'Montpelier', 'Virginia': 'Richmond',
	'Washington': 'Olympia', 'West Virginia': 'Charleston',
	'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# generate quiz files
numberOfQuizzes = 5;
for quizNumber in range(numberOfQuizzes):
	# create quiz and answer key files
	quizFile = open('Quiz%s.txt' % (quizNumber + 1), 'w')
	answerKeyFile = open('QuizAnswers%s.txt' % (quizNumber + 1), 'w')

	# shuffle order of the states
	states = list(stateCapitals.keys())
	random.shuffle(states)

	# loop through all 50 states to make a question for each
	for questionNumber in range(50):
		# get right and wrong answers
		correctAnswer = stateCapitals[states[questionNumber]]
		
		wrongAnswers = list(stateCapitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)

		answerOptions = wrongAnswers + [correctAnswer]

		random.shuffle(answerOptions)

		# write question and answer options to quiz files
		quizFile.write('%s. What is the capital of %s\n' % (questionNumber + 1, states[questionNumber]))

		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

		quizFile.write('\n')

		# write answer key to a file
		answerKeyFile.write('%s. %s\n' % (questionNumber + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerKeyFile.close()
