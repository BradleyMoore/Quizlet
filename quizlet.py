#!c:\python27\python.py -u

import os
import sys
import random

line_skips = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
random_question = ''
random_index = 0
temp_question = ''
questions = []
quiz_file = open('quizlet.txt', 'r')

for line in quiz_file:
	questions.append(line.strip())

for i in xrange(len(questions)):
	random_index = random.randint(i, len(questions)-1)

	random_question = questions[random_index]
	temp_question = questions[i]

	questions[random_index] = temp_question
	questions[i] = random_question

for question in questions:
	print line_skips
	print question
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	raw_input('Press enter to go to next question...')