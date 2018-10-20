import json
from pprint import pprint

# with open('./jsonExample.json') as f:
# 	data=json.load(f)
#
# pprint(data)


def matchFields(cv_text,category):

	arg3 = cv_text
	arg4 = category
	acd = [arg3.lower(), arg4];
	finalArray = []
	#Hardcoded business fields (may be in separated files) [informatica,comercial,sanidad, turismo]
	business = {
	'informatica':['php', 'java', 'javascript', 'js','android', 'ios','c++', ' c ', 'c#','perl','erlang','big data','sql','mysql','sqlite','.net','matlab',' r ','swift','assembly','ruby','delphi',' go ','scratch','visual basic','visualbasic'], 
	'comercial':['marketing','e-marketing', 'social media', 'comunicacion','emprendedor','emprendedora','aspiraciones','ilusionada','ventas','immobiliaria'],
'sanidad':['audioprotesista','salud','audiologia','cardiologia'],'turismo':['viajar','idiomas','representacion']
	}

	print ('The matches are:')

	#Match loop:
	for elem in business[arg4]:
		if elem in acd[0]:
			finalArray.append(elem)
	print (finalArray)
	return finalArray

#matchFields()





