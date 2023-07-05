

def convert_dec_to_base(num, base):
	char_base="0123456789ABCDEF"
	base_num= ""
	n = int(num)
	while n>0:
		base_num+=base_num.join( char_base[n%base])
		n//=base
		
	return base_num[::-1]

def base_n_to_dec(num, base):
	a = int(num, base)
	return a

print(convert_dec_to_base("49",3))
print(convert_dec_to_base("1234", 16))
print(base_n_to_dec("1211", 3))
print()