import requests
from bs4 import BeautifulSoup as bs
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def wth():
    s = []
    r = requests.get('https://www.yandex.ru/weather/segment/details?\
    offset=0&lat=55.753215&lon=37.622504&geoid=213&limit=10')
    soup = bs(r.content,'lxml')
    print(soup) 
    for card in soup.select('.card:not(.adv)'):
        date = ''.join([i.text for i in card.select('[class$=number],\
        [class$=month]')]
        )
        s += date
        temps = list(zip(
        [i.text for i in card.select\
        ('.weather-table__daypart')]
        ,[i.text for i in card.select\
        ('.weather-table__body-cell_type_feels-like\
        .temp__value')])
        )
        return str(s + temps).split(',')
def main():
    
    vk_session = vk_api.VkApi(token=\
    'bdd6a9ad98b09eb8c1c02b0a29f9865e66ba6105036323e00fcff21f0f7e83239ce4e67297bdb0c6f96a8')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text == 'start':
            print('New from {}, text = {}'.format(event.user_id,event.text))

            vk.messages.send(
                user_id = event.user_id,
                random_id = get_random_id(),
                message = 'Здравствуйте, ' + \
                    vk.users.get(user_id = event.user_id)[0]['first_name'] + \
                    ' посылайте команды, командой help выводится список всех\
                    команд.'
                    )
        if event.type == VkEventType.MESSAGE_NEW and event.text == 'help':
            print('New from {}, text = {}'.format(event.user_id,event.text))
            vk.messages.send( user_id = event.user_id,
                              random_id = get_random_id(),
                              message = 'weather - показывает погоду\n\
                              virus - показывает статистику по COVID-19\n\
                              why - потому что текст')
                                         
        if event.type == VkEventType.MESSAGE_NEW and event.text == 'why':
            print('New from {}, text = {}'.format(event.user_id,event.text))
            vk.messages.send( user_id = event.user_id,
                              random_id = get_random_id(),
                              message = 'Потому что автор любит текстовые инте\
рфейсы набодобие bash'
                              )

        if event.type == VkEventType.MESSAGE_NEW and event.text == 'wth':
            print('New from {}, text = {}'.format(event.user_id,event.text))
            vk.messages.send( user_id = event.user_id,
                              random_id = get_random_id(),
                              message = wth()
                              )


if __name__ == '__main__':
    main()
