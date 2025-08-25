class demo:
    def largest(self,n):
        length=len(n)
        large=-1
        slarge=-1
        
        for i in range(length):#34
            if n[i]>large: #45>3
                slarge=large#3
                large=n[i]#45
            elif n[i]<large and n[i]>slarge:
                slarge=n[i]
                
        return slarge
ob=demo()
print(ob.largest([3,45,6,34,6,1,35]))

        
