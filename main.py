class lambda_NFA:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def lambdaClosure(self, state):#all the states reachable only with lambda(NULL) transitions
        L = set([state])

        def back(aux_state):
            nonlocal L
            for i in self.delta[(aux_state, '$')]:
                if i not in L:
                    L.add(i)
                    back(i)
        back(state)
        return L

    def roads(self, state, letter): #all the states reachable with a single, given letter, from a specified state
        L = self.lambdaClosure(state)
        newL = set([])
        for i in L:
            if (i, letter) in self.delta:
                for q in self.delta[(i, letter)]:
                    newL.add(q)
        finalL = set([])
        for q in newL:
            finalL = finalL.union(self.lambdaClosure(q))
        if len(finalL) == 0:
            return "#"  # '#'=null set
        return finalL

    def lambda_table(self):#making the table of the lambda-NFA as a dict of dict
        table = {}
        for q in self.Q:
            q = str(q)
            table[q] = {}
            for letter in self.sigma:
                table[q][letter] = self.roads(int(q), letter)
        return table

    def to_dfa_table(self):
        table = self.lambda_table()
        dfa_table = {}
        l = set(
            ["".join([str(x) for x in self.lambdaClosure(self.q0) if str(x) != '#'])])# l is going to be a set of newly added states which are to be computed in the table

        ok = 1
        while ok: 
            ok = 0
            l1 = l.copy()
            for state in l1:
                dfa_table[state] = {}
                for letter in self.sigma:
                    new_state = set([])
                    for i in state:
                        new_state = new_state.union(table[i][letter])
                    new_state = "".join([str(x)
                                        for x in new_state if str(x) != '#'])
                    dfa_table[state][letter] = new_state
                    if new_state not in dfa_table:
                        l.add(new_state)
                        ok = 1
            l.remove(state)
        F=set([])
        for i in dfa_table: #finding the new q0 and new final states
            if str(self.q0) in i:
                q0=i
            for k in i:
                if int(k) in self.F:
                    F.add(i)
        return dfa_table,q0,F

    def run(self, word): # checks if a word is accepted and provides all the possible ways in which it can be computed correctly
        ok = False
        D = []

        def wordCheck(word, q, L=[]):
            L.append(q)
            nonlocal ok
            nonlocal D
            if word == "":
                if q in self.F:
                    ok = True
                    D.append(L)
            else:
                if (q, word[0]) in self.delta:
                    for state in self.delta[(q, word[0])]:
                        l1 = L[::]
                        wordCheck(word[1:], state, l1)
        wordCheck(word, self.q0)
        return D, ok

    def parseWords(self):
        g = open("words.in", 'r')
        for word in g:
            word = word.strip()
            new_word = "$"
            for i in word:
                new_word += i+"$"
            L, ok = automata.run(new_word)
            if ok == True:
                print(
                    f"\nThe word --{word}-- has been accepted and the paths are:")
                for path in L:
                    print(*path, sep="-")
            else:
                print(f"\nThe word --{word}-- has been rejected.")
        g.close()


f = open("automata.in", 'r')
g = open("words.in", 'r')
Q = [int(x) for x in f.readline().split()]
sigma = f.readline().split()
q0 = int(f.readline())
F = [int(x) for x in f.readline().split()]
delta = {}
for l in f:
    l = l.split()
    if (int(l[0]), l[1]) in delta:
        delta[(int(l[0]), l[1])].append(int(l[2]))
    else:
        delta[(int(l[0]), l[1])] = [int(l[2])]
for stare in Q: #adding lambda transitions from every state to itself
    if (stare, '$') in delta:
        delta[(stare, '$')].append(stare)
    else:
        delta[(stare, '$')] = [stare]
automata = lambda_NFA(Q, sigma, delta, q0, F)
print(automata.to_dfa_table())
f.close()
