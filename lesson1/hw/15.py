text = 'some string'

first_occurance = text.find('zip')
second_occurance = text.find('zip',first_occurance+1)

print second_occurance
