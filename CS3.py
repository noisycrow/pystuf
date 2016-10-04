slang = ['cheerio', 'pip pip', 'smashing']
print(slang)
slang.append('cheeky')
slang.append('yonks')
print(slang)
slang.remove('cheeky')
print(slang)
del slang[3]
print(slang)
del slang[:2]
print(slang)

print('Dictionaries')
slang = {'cheerio': 'goodbye', 'knackered': 'tired'}
result = slang.get('bloody')

if result:
    print(result)
else:
    print("Key doesn't exist")
