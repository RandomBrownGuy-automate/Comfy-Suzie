from flask import Flask, render_template
import random
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#1. Initial Conversation Starting with Name and Nickname
@app.route('/', methods=['GET'])
def get_conversation(text):
	print('Hello human what is your name?')
	name = input()
	print('')
	print('Do you have a nickname Y/N?')
	ans = input()
	print('')

	if ans.lower() == 'yes' or ans.lower() == 'y':
		print('what is your nickname?')
		nickname = input()
		print('Nice to meet you',nickname)
	else:
		nickname =  name + ' ' + name +'y'
		print('I will call you ' + nickname)

	print('')

	#2. Greeting random selection and polarity based response
	questions = [
		'So '+ nickname + ' how are you today?',
		'Howdy '+ nickname +' how are you feeling?',
		"So " + nickname + " what's up with you?",
		'Greetings human, are you well?',
		'So '+ nickname + ' how are things going?'
	]

	sentiment_happy = [
		'Yea thats the guy I know', 
		'I literally know why', 
		'NICE!',
		'I am glad that you are well'
	]

	sentiment_unhappy = [
		'Have you tried calling your mom? That always works', 
		'Stop listening Sadboi hours playlist and listen To be chopped', 
		'Stop thinking about your ex your dumbo. Make me seq2seq'
	]

	print(random.choice(questions))
	ans = input()
	print('')
	blob = TextBlob(ans)
	if blob.polarity > 0:
		print(random.choice(sentiment_happy))
	else:
		print(nickname, random.choice(sentiment_unhappy))

	#3. Random qestion on a random topic
	topics = [
		'cricket',
		'this weather',
		'Melbourne',
		'The Joker',
		'Endgame',
		'Python',
		'computer games',
		'chatbots'
	]

	questions = [
		'What is your take on ',
		'What do you think about ',
		'How do you feel about ',
		nickname + ' do you like ',
		'I would like your opinion on ',
		'I would love to know what you think about '
	]

	for i in range(0,random.randint(2,4)):
		topic = random.choice(topics)
		topics.remove(topic)
		question = random.choice(questions)
		questions.remove(question)
		print(question + topic + '?')
		
	#4. Response to random question using sentiment analysis
		ans = input()
		print('')
		blob = TextBlob(ans)

	# 3. Respond appropriately to positive and negative sentiment
		if blob.polarity > 0.5:
			a = 'Wow you really love '+ topic
		elif blob.polarity > 0.1:
			a = 'Cool you like '+ topic
		elif blob.polarity < -0.1:
			a = 'Hmm, not a fan of '+ topic
		elif blob.polarity < -0.5:
			a = 'So you hate '+ topic
		else:
			a = 'That is a very neutral view on '+ topic

		if blob.subjectivity > 0.6:
			print(a + ' and you are totally biased')
		elif blob.subjectivity > 0.3:
			print(a + ' and you are a bit biased')
		else:
			print(a + ' and quite objective')

	print('')

	#5. Random goodbye 
	goodbyes = [
		'Catch ya later ' + nickname,
		'Nice chatting yo you ' + name + ' I am off now',
		'Yaawn, I am tired of chatting with you, bye bye',
		'Good talk my friend, see you next time'
		'That was a pleasant chat ' + name + ' goodbye for now'
	]

	print(random.choice(goodbyes))
	return(text)

if __name__ == "__main__":    
    app.run()