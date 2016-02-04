from jinja2 import Template
import lunar
import datetime
import time
import db
import os
import random
from Person import create_person
from sendmail import send_mail

templatePathnameGroup = []

def init_template_pathname_group():
	templatePathnameGroup = filter(lambda x:x.endswith('.tpl'), os.listdir('./mail-templates'))

def main():
	now = time.localtime()
	now = datetime.datetime(now.tm_year, now.tm_mon, now.tm_mday)
	lunar_now = lunar.get_lunar_date(now)
	now = (now.year, now.month, now.day)
	
	log('now', now)
	log('lunar_now', lunar_now)

	personGroup = []

	sql1 = 'select name, sex, birthday, calendar, mail from person where birthday="%04d-%02d-%02d" and calendar="阳历"' % (now[0], now[1], now[2])
	sql2 = 'select name, sex, birthday, calendar, mail from person where birthday="%04d-%02d-%02d" and calendar="阴历"' % (lunar_now[0], lunar_now[1], lunar_now[2])
	for sql in (sql1, sql2):
		db.select(sql, lambda item:personGroup.append({'name':item[0],'sex':item[1],'birthday':item[2],'calendar':item[3],'mail':item[4]}))
	
	init_template_pathname_group()

	for person in personGroup:
		templatePathname = random.choice(templatePathnameGroup)
		template = Template(open(templatePathname, 'rt').read())
		text = template.render(person = create_person(
				person['name'],
				person['sex'],
				person['birthday'],
				person['calendar'],
				person['mail'],
				now,
				lunar_now
			) 
		)
		send_mail('niu2x@346-1.com', person['mail'], 'Happy Birthday To You!', text)

if __name__ == '__main__':
	main()
