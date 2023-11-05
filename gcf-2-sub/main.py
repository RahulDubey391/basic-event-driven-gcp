import json
from google.cloud import pubsub_v1
import requests
import pandas as pd


def getMessages(event, context):

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path('<PROJECT-ID>', 'my-gcf-topic-2-sub')

    def callback(message):
        message_dict = json.loads(message.data.decode('utf-8'))
        message_str = json.dumps(message_dict)
        request_batch = message_dict['batch']
        print('Batch length: ',len(request_batch))

        for i in request_batch:
            print(i)
            
        message.ack()
    
    flow_control = pubsub_v1.types.FlowControl(max_messages=1)
    future = subscriber.subscribe(subscription_path, callback=callback,flow_control=flow_control)
    try:
        future.result()
        return 'Done'
    except KeyboardInterrupt:
        future.cancel()
        return 'Failed'