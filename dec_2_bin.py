"""Convert decimal number to binary"""
def dec_2_bin(num):
	temp = int(num)
	bin_num=""
	while temp>0:
		i = temp% 2
		temp//=2
		bin_num+=str(i)		
	return bin_num[::-1]
	
num= int(input("Enter a decimal number::"))
print(dec_2_bin(num))