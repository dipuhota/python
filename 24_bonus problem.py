sal=int(input('enter your salary'))
gen=input('enter your gender')

if gen=='m':
    bonus=0.05*sal
else:
    bonus=0.10*sal


if sal<15000:
    print('u will gate extra 3% bonus because u r sal is less then 15000')
    bonus=bonus+0.03*sal


sal=bonus+sal

print('sal is',sal)