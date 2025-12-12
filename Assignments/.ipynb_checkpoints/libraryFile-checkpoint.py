class Multifunction():
    def Subfields():
        List=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for each in List:
            print(each)
            
    def OddEven():
        number=int(input("Enter a number: "))
        if(number%2==0):
            result= str(number)+" is Even number"
        else:
            result= str(number)+" is Odd number"
        print(result)
        return result

    def Elegible():
        Gender=input("Your Gender")
        Age=int(input("Your Age"))
        if((Gender.lower() =='male'and Age>22)or (Gender.lower() =='female'and Age>18)):
            Result= "ELEGIBLE"
        else:
            Result= "NOT ELEGIBLE"
        print(Result)
        return Result
        
    def Percentage():
        Subject1=int(input("Subject1 ="))
        Subject2=int(input("Subject2 ="))
        Subject3=int(input("Subject3 ="))
        Subject4=int(input("Subject4 ="))
        Subject5=int(input("Subject5 ="))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        print("Total:",(Total/500)*100)
        return (Total/500)*100
         
    def AreaOfTriangle(height,breadth):
        print("Height: ",height)
        print("Breadth: ",breadth)
        print("Area Formula: (height*breadth)/2")
        return ((height*breadth)/2)
   
    def PerimeterOfTriangle(height1,height2,breadth):
        print("Height1: ",height1)
        print("Height2: ",height2)
        print("Breadth: ",breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        return height1+height2+breadth
  
    def triangle():
        Area=Multifunction.AreaOfTriangle(32,34)
        print("Area of Triangle: ",Area)
        Perimeter=Multifunction.PerimeterOfTriangle(2,4,4)
        print("Perimeter of Triangle: ",Perimeter)