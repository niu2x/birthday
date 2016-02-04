def create_person(name, sex, birthday, calendar, mail, now, lunarNow):
	person = []
	person['name'] = name
	person['sex'] = sex
	person['calendar'] = calendar
	person['mail'] = mail
	person['now'] = {
		'year':int(now[0]),
		'month':int(now[1]),
		'day':int(now[2])
	}
	person['lunarNow'] = {
		'year':int(lunarNow[0]),
		'month':int(lunarNow[1]),
		'day':int(lunarNow[2])
	}
	person['birthday'] = birthday.split('-')
	person['birthday'] = {
		'year':int(birthday[0]),
		'month':int(birthday[1]),
		'day':int(birthday[2])
	}
	if person['calendar'] == u'阳历':
		person['age'] = self.now['year'] - self.birthday['year']
	else:
		person['age'] = self.lunarNow['year'] - self.birthday['year']
	return person
