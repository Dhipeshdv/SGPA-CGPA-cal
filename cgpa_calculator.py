class Marks:
    l=[]
    sum=0
    csum=0
    def __init__(self,course):
        self.course=course

    def grade_cal(self,grade):
        match grade:
            case 'O':
                return 10
            case 'A+':
                return 9
            case 'A':
                return 8
            case 'B+':
                return 7
            case 'B':
                return 6
            case default:
                raise "Error !! Wrong Grade"

    def list(self):
        for i in range(self.course):
            name=input("Enter Course Name:")
            print("Enter Grade O/A+/A/B+/B/C ")
            grade=self.grade_cal((input().upper()))
            credit=int(input("Enter no of credit for the course(1/2/3/4):"))
            self.csum+=credit
            self.sum+=grade*credit
            self.l.append([name,grade,credit])

    def printall(self):
        for i in self.l:
            print(i)

    def sgpa(self):
        print(self.sum/self.csum)




a=Marks(8)

a.list()
a.printall()
a.sgpa()


