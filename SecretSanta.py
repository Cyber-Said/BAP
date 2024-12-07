# О чем код?
# наша задача устроить Тайного Санту, условия игры те же самые
# условие 1: участник не может подарить подарок самому себе
# условие 2: участник может дарить подарок только 1 человеку

# остальное уже понятно, взглянув на код



import random

COUNT_OF_MEMBERS = 4
GRAPH = [[0 for x in range(COUNT_OF_MEMBERS)] for y in range(COUNT_OF_MEMBERS)]

class Member:
    def __init__(self, index):
        self.index = index
        self.loyality = round(random.random(), 1)   
        self.empathy = random.randint(0, 10) 
               
    def set_taker(self, taker, members):
        if GRAPH[taker][self.index] == 0 and taker != self.index:   # если получатель ещё не имеет статус получателя в отношение к текущему отправителю, что определяется цифрой 0
            GRAPH[taker][self.index] = -1                           # то этот статус он приобретает, с помощью цифры -1
            GRAPH[self.index][taker] =  1                           # отправитель получает статус отправителя, с помощью цифры 1
            self.taker_member = taker                               # это нужно для метода __str__ класа Member
            return True                                             # это нужно для функции create_edges
            
    def __str__(self):
        return f'\nindex: {self.index}\nempathy: {self.empathy}\nloyality: {self.loyality}\ntaker: {self.taker_member}\n'    
    

def main():
    members = create_members()
    create_edges(members)
    rating_list = rating(members)
    print_data(rating_list, members)

def create_members():
    members = []
    for i in range(COUNT_OF_MEMBERS):
        member = Member(i)
        members.append(member)
    return members
    
def create_edges(members):
    used_members = members[:]
    i = 0
    while i != len(members):
        random_taker = random.choice(used_members)
        if members[i].set_taker(random_taker.index, members):
            used_members.remove(random_taker)
            i += 1
            
     
def rating(members):
    rating_list = [i.loyality * i.empathy for i in members]
    return rating_list
       
def print_data(rating_list, members):
    print("Граф отношений участников", GRAPH)
    
    for i in members:
        print(i)
        
    success_rate = sum(rating_list) / len(rating_list)
    print(f'Secret Santa succesfull: \n{success_rate}')
        
if __name__ == '__main__':
    main()