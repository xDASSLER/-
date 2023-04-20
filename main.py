import vk_api
import pymysql
from config import host, user, bdname
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
vk_session = vk_api.VkApi(token = "vk1.a.zY1tU3cleZSSSrbmXuBuGmdkeYoLQw_q0gR_UtDe5MNePk4ZbR7LDu42ozf3-oLX8ZvhLiu8VG8I-oO017WB9lnEnsf3egNJXVIQRXu5Dp2WPx7m_j7AwG16fIRJ_un1RFi0yGFZ9a9saIYfV0oncKr6OXci3SoPRM8bMZOOHVdWPNA-iWyFjQPpUn8Rvv3ZnLd4sIHpFggKjBbFs7-13Q")

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        database=bdname,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("good")

    try:
        cursor = connection.cursor()

        with connection.cursor() as cursor:

            sql = "SELECT `EnglishWord` FROM `word for bot`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            print("Всего строк = ", len(result))
    finally:
        connection.close()

except Exception as ex:
    print(ex)

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        database=bdname,
        cursorclass=pymysql.cursors.DictCursor
        )
    print("good")

    try:
        cursor = connection.cursor()

        with connection.cursor() as cursor:

            sql = "SELECT `RussianWord` FROM `word for bot`"
            cursor.execute(sql)
            result1 = cursor.fetchall()
            print(result1)
            print("Всего строк = ", len(result1))
    finally:
        connection.close()

except Exception as ex:
    print(ex)


session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text, "random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "привет":
                send_some_msg(id, "Привет, напиши любое слово, например 'начать'!")
                break
            else:
                send_some_msg(id, "Для старта с ботом, напиши 'привет'")

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "продолжить" or "начать":
                a = randint(0,14)
                send_some_msg(id,"попробуй перевести слово - ")
                send_some_msg(id, result[a]['EnglishWord'])
                for event in longpool.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            msg = event.text.lower()
                            id = event.user_id
                            if msg == result1[a]['RussianWord']:
                                send_some_msg(id, "Молодец!, чтобы продолжить напиши любое слово, например 'продолжить'")
                                break
                            else:
                                send_some_msg(id, "Неправильно!")
                                send_some_msg(id, "чтобы продолжить напиши 'продолжить'")
                                break