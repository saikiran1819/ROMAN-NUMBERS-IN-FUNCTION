### --> ROMAN NUMBERS
def rom(n):
    nums=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i=len(nums)-1
    roman_num=''
    while n!=0:
        if nums[i]<=n:
            roman_num+=roman[i]
            n-=nums[i]
        else:
            i-=1
    return roman_num
print(rom(49))
print(rom(13779))
print(rom(7836))
print(rom(7))
roman=int(input('Enter a number:-'))
print(rom(roman))
