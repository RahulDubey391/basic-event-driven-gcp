import requests
import json
import logging
import pandas as pd
from google.cloud import pubsub_v1


def chunks(lst, chk_size):
    chunk_list = []
    for index in range(0, len(lst), chk_size):
        chunk_list.append(lst[index:index + chk_size])
    return chunk_list

def message_publisher(message):

    # Convert the message dictionary to a JSON string
    message_str = json.dumps(message)

    # Set up the Pub/Sub client and topic
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('<PROJECT-ID>', 'my-gcf-topic-2')
    
    # Publish the message to the topic
    future = publisher.publish(topic_path, message_str.encode('utf-8'))

def publishMessages():
    try:
        messages = []
        for i in range(0, 20000):
            messages.append(f'Hi, this is message %s'%i)

        chunk_list = chunks(messages,250)
        for i,j in enumerate(chunk_list):
            message = {'batch':j}
            message_publisher(message)

        return True
    
    except Exception as e:
        logging.exception(e)
        return False


def getRequest(request):
    try:
        if publishMessages():
            return {'message':'Success'}
        else:
            return {'message':'Failed'}

    except Exception as e:
        print('Got the exception: \n',e)
        return {
            'message':str(e)
        }