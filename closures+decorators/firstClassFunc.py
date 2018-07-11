# Code adapted from Corey Shafer
#Allow us to treat functions like a object
def html_tag(tag):

	def wrap_text(msg):
		print('<{0}>{1}</{0}'.format(tag, msg))

	return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print(h1('Another Headline'))

print_p = html_tag('p')
print_p('Test Paragraph')