Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name='GUY'
name
'GUY'
print(name)
GUY
type(name)
<class 'str'>
name.lower()
'guy'
name.upper()
'GUY'
#name.ctrl+space เลือกเอา
friend='gg'
print('สวัสดีสมชาย')
สวัสดีสมชาย
>>> print('สวัสดี'+friend)
สวัสดีgg
>>> money=10
>>> print('สมชายยืมเงิน'+str(money))
สมชายยืมเงิน10
>>> print('{}ยืมเงิน{}บาท'.format(friend,money))
ggยืมเงิน10บาท

>>> print(f'{friend}ยืมเงิน{money}บาท')
ggยืมเงิน10บาท
>>> 
>>> print(f'{friend}ยืมเงิน{money}บาท')
ggยืมเงิน10บาท
>>> print(f'{friend} ยืมเงิน {money}บาท')
gg ยืมเงิน 10บาท
>>> money=140486463046987
>>> print(f'{money:,}')
140,486,463,046,987
>>> print(f'{money:,.2f}')
140,486,463,046,987.00
