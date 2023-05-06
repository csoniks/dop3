from functools import reduce
all_news = [{'zag': 'Курс биткоина вырос до 1000 долларов. 5', 'positive': 5},
    {'zag': 'В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока". 10', 'positive': 10},
    {'zag': 'Где-то далеко идут дожди. 10', 'positive': 10},
    {'zag': 'В Новосибирске из автобуса сбежала кондуктор. 7', 'positive': 7},
    {'zag': 'Самолет «Почты России» вылетел с опозданием в несколько месяцев. 1', 'positive': 1},
    {'zag': 'Козёл Тимур подружился с тигром Амуром. 20', 'positive': 20},
    {'zag': 'Инженерам из Space X удалось посадить первую ступень ракеты на землю. 10', 'positive': 10},
    {'zag': 'Самолёты сбиваются с пути. 20', 'positive': 20},
    {'zag': 'Просто не дай ему уйти. 21 ', 'positive': 21}]

published_news = [] #сюда добавляем только подходящие для публикации списки новостей
def can_publish_news(news):
    if not published_news:
        return True
    else:
        previous_sentiment = reduce(lambda x, y: x if x > y else y, [i['positive'] for i in published_news]) # выб наиб из нашей проверяемой и уже стоящей в списке
        return (news['positive'] > previous_sentiment) #проверяет чтобы наша проверяемая новость была позитивнее чем предыдущая в нашем списке
        #возвращает True/False

for slovar_news in all_news:
    if can_publish_news(slovar_news) == True:
        published_news.append(slovar_news) #на выходе список из словарей-новостей
print("Миша репостнул: ")
print()
for news in published_news:
    print(news['zag'])