
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

def solution(n, b):
    #Your code here
    minions_list=[]
    num = n
    k = len(n)
   # minion_id = int(num,b)
    base = b
    z = "1"
    while (z not in minions_list):
        temp = "".join(sorted(num))
        x = temp[::-1]
        y = temp
        
        z = convert_dec_to_base(str(base_n_to_dec(x,base)-base_n_to_dec(y,base)),base)
        
        
        z = z.zfill(k)
        minions_list.append(x)
        minions_list.append(y)
        if z==num:
        	minions_list.append(z)
        	break
        num = z
        
    print (minions_list, z, num, len(minions_list)/2)
    return


test_2 = "210022" #3 3
base_2 = 3
test_1="1211" #10 1 1211
base_1 = 10
print (solution(test_2,base_2))
print (solution(test_1,base_1))
