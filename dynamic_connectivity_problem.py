#main Function
def main():
    x= input()
    union_find_class = UF(x)
    
    while (len(input)==0):
        a=input
        b=input
        if (union_find_class.connected(a,b)==False):
            union_find_class.union(a,b)
            print(a+" ",b)
    
#union Find Class 
class UF:
    def __init__(self,x:int) -> None:
        self.number_of_Individual_components = x

    number_of_Individual_components=0
    components_arr=[]

    def union(self,a:int,b:int)->None:
        unioned_list=[a,b]
        self.components_arr.append(unioned_list)

    def connected(self,a:int,b:int)->bool:
        for a,b in self.components_arr:
            if a and b in self.components_arr:
                return True
            else:
                return False

main()