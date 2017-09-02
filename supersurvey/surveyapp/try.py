nr_Questions = Question.objects.filter(type='NR', deleted=False)
averages = []
for q in nr_Questions:
	nr_Answers = Answer.objects.filter(question=q)
	count = 0
	total = 0
	for ans in nr_Answers:
		count += 1
		total += int(ans.answer)
	average = (q.id, total/count)
	averages.append(average)

def mc_question_distribution(id):
	q = Question.get(pk=id)
	mc_Answers = Answer.objects.filter(question=q)
	distribution = []
	for i, variant in enumerate(question.variants):
		count = mc_Answers.filter(answer=variant).count()
		distribution.append((i, variant, count))
	return distribution

#def session_answers(id):
#	answers = Answer.objects.filter

