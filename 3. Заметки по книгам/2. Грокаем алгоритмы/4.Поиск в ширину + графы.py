from  collections import deque  # создает очередь

graf = {'я': ['филипп', 'сема', 'никита'], "филипп": ["ярик","артем"],'сема':["даник"], "никита":['тима']}

# searce_q = deque()
#
# searce_q += graf["филип"]
# print(searce_q)
#


def search(name):
    searce_q = deque()
    searce_q += graf[name]

    searched = []
    while searce_q:
        person = searce_q.popleft()

        if person not in searched:
            if 'ан' in person:
                print(person + ' - Вот он!')
                return True
            else:
                try:
                    searce_q += graf[f'{person}']
                    searched.append(person)
                except:
                    continue
    return False

search('я')