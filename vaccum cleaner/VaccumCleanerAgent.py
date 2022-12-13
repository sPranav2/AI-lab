#vaccum cleaner agent
class Environment():
    locationCondition={'a':'0','b':'0'}
    cost=0
    def __int__(self):
        self.cost=0

    def locationstatus(self):
        self.locationCondition['a']=input('enter condition of room a \n')
        self.locationCondition['b']=input('enter condition of room b \n')

    def checkRoom(self,room):
        if self.locationCondition[room]=='0':
            print("room",room,"is clean")
            return 0

        elif self.locationCondition[room]=='1':
            print("room", room, "is dirty")
            self.cost+=1
            self.locationCondition[room]='0'
            print('cost of cleaning',self.cost)
            return 1

    def moveAndAct(self,room):
        if room=='a':
            self.cost+=1
            print('going to room b')
            if self.checkRoom('b')==0:
                print('at room b. room is clean')
                print('cost for moving',self.cost)
            else:
                print('at room b, room is dirty')
                self.locationCondition['b']=0
                print("cost for moving and cleaning",self.cost)




        elif room=='b':
            self.cost+=1
            print("going to room a")
            if self.checkRoom('a')==0:
                print('at room a. room is clean')
                print('cost of moving',self.cost)
            else:
                print('at room a. a is dirty')
                self.locationCondition['a'] = 0
                print('cost of moving and cleaning',self.cost)


def main():
    print("vaccum cleaner agent [0: dirty, 1:clean]")
    e=Environment()
    e.locationstatus()
    e.checkRoom('a')
    e.moveAndAct('a')
    #e.checkRoom('b')
    e.moveAndAct('b')
    print('total cost: ',e.cost)


main()





