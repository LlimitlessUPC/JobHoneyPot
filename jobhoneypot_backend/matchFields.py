def matchFields():
	#Given by HTTP POST REQUEST 
	arg1='FancyClientName'
	arg2="informatica"	#That's the important one (business)
	arg3='this is my CV Im so android cute I know and PHP and C++. Byerrr R salud audiologia marketing '
	
	acd = [arg1, arg2, arg3.lower()];
	finalArray = []
	#Hardcoded business fields (may be in separated files) [Informatica,comercial,sanidad, turismo]
	business = {
	'informatica':['php', 'java', 'javascript', 'js','android', 'ios','c++', ' c ', 'c#','perl','erlang','big data','sql','mysql','sqlite','.net','matlab',' r ','swift','assembly','ruby','delphi',' go ','scratch','visual basic','visualbasic'], 
	'comercial':['marketing','e-marketing', 'social media', 'comunicacion','emprendedor','emprendedora','aspiraciones','ilusionada','ventas','immobiliaria'],
'sanidad':['audioprotesista','salud','audiologia','cardiologia'],'turismo':['viajar','idiomas','representacion']
	}

	print ('The matches are:')

	#Match loop:
	for elem in business[arg2]:
		if elem in acd[2]:
			finalArray.append(elem)
	print (finalArray)
	return finalArray

matchFields()





