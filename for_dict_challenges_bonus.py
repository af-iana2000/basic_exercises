"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem

from collections import Counter

def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

messages = generate_chat_history()
#print(messages[0-10])

# Вывести айди пользователя, который написал больше всех сообщений.
def find_user_with_most_messages(data, key):
    values = [d[key] for d in data]
    counter = Counter(values)
    value, count = counter.most_common(1)[0]
    if value is None:
        value, count = counter.most_common(2)[1]
    return value, count
user, messages_count = find_user_with_most_messages(messages, 'sent_by')
print(f'1. Пользователь с ID {user} написал {messages_count} сообщений(-я)')

# Вывести айди пользователя, на сообщения которого больше всего отвечали.
def find_user_with_most_replies(data):
    message_replied, count_message = find_user_with_most_messages(data, 'reply_for')
    for message in data:
        if message.get('id') == message_replied:
            user_id = message.get('sent_by')
            return message_replied, user_id, count_message
message_replied, user_id, count_message = find_user_with_most_replies(messages)
print(f'2. На сообщение {message_replied} пользователя с ID {user_id} ответили {count_message} раз(-а)')

# Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def find_user_most_popular(data):
    user_seen_by = {
        'user_id': '',
        'seen_by': [],
        'uniq_followers': 0
    }
    users_seen_by = []
    for message in data:
        users_only = [d.get('user_id') for d in users_seen_by]
        if message.get('sent_by') in users_only:
            for user in users_seen_by:
                if user['user_id'] == message.get('sent_by'):
                    user['seen_by'].extend(message.get('seen_by'))
                    user['uniq_followers'] = len(set(user['seen_by']))
        else:
            user_seen_by['user_id'] = message.get('sent_by')
            user_seen_by['seen_by'] = message.get('seen_by')
            user_seen_by['uniq_followers'] = len(set(user_seen_by['seen_by']))
            users_seen_by.append(user_seen_by)
    user = max(users_seen_by, key=lambda x: x['uniq_followers'])
    return f'Сообщения пользователя с ID {user['user_id']} видело наибольшее количество уникальных пользователей: {user['uniq_followers']}'
print(f'3. {find_user_most_popular(messages)}')

# Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
def find_popular_time(data):
    messages_per_time = {
        'morning': 0,
        'afternoon': 0,
        'evning': 0
    }
    for message in data:
        if message.get('sent_at').time().hour <= 12:
            messages_per_time['morning'] += 1
        elif 12 <= message.get('sent_at').time().hour <= 18:
            messages_per_time['afternoon'] += 1
        elif 18 <= message.get('sent_at').time().hour:
            messages_per_time['evning'] += 1
    popular_time = max(messages_per_time, key=messages_per_time.get)
    num_messages = messages_per_time.get(popular_time)
    return popular_time, num_messages
popular_time, num_messages = find_popular_time(messages)
print(f'4. Больше всего сообщений писали в это время суток: {popular_time} ({num_messages})')

# Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
from collections import defaultdict
def thread_length(message_id, parent_dict):
        if message_id not in parent_dict:
            return 1
        lengths = [thread_length(child_id, parent_dict) for child_id in parent_dict[message_id]]
        return 1 + max(lengths)

def find_popular_message(data):
    messages_and_answers = defaultdict(list)
    for message in data:
        parent = message['reply_for']
        if parent is not None:
            messages_and_answers[parent].append(message['id'])   
    parents_only = [message['id'] for message in messages if message['reply_for'] is None]
    max_len = 0
    longest_roots = []
    for parent in parents_only:
        length = thread_length(parent, messages_and_answers)
        if length > max_len:
            max_len = length
            longest_roots = [parent]
        elif length == max_len:
            longest_roots.append(parent)
    return longest_roots[0], max_len
longest_roots, max_len = find_popular_message(messages)
print(f'5. Сообщение с ID {longest_roots} породило самую длинную цепочку ответов - {max_len}')

if __name__ == "__main__":
    generate_chat_history()
