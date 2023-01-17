#implement unification in First Order Logic

class Main():
    predicate=''
    predicate1=''
    predicate2=''
    predicate1suffix=''
    predicate2suffix=''
    def initialise(self,e1,e2):
        self.predicate1 = e1.split('(')
        self.predicate2 = e2.split('(')
    def checkPredicate(self):
        if(self.predicate1[0]==self.predicate2[0]):
            self.predicate=self.predicate1[0]
            self.predicate1suffix=self.predicate1[1].split(')')[0]
            self.predicate2suffix=self.predicate2[1].split(')')[0]
            return True
        else:
            return False

    def checkSubject(self):
        if (self.predicate1suffix == self.predicate2suffix):
            return False
        else: return True




print('enter expressions')
e1=input()
e2=input()
m=Main()
m.initialise(e1,e2)
if(m.checkPredicate()):

    if(m.checkSubject()):
        print('substitution: {',m.predicate1suffix,'/',m.predicate2suffix,'}')
    else:
        print('subjects same/conflicting, unification not possible')

else:
    print('unequal predicates, unification not possible')


