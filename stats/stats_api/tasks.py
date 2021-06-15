import pika
from stats_api.serializers import RecordedGameSerializer
from .models import RecordedGame
from celery import shared_task

# def consume():
#     print("WORKING!!")
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters(host='10.64.4.147'))

#     channel = connection.channel()

#     channel.queue_declare(queue='stats_queue', durable=True)

#     def callback(ch, method, properties, body):
#         serializer = RecordedGameSerializer(data=body)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         ch.basic_ack(delivery_tag=method.delivery_tag)

#     channel.basic_qos(prefetch_count=1)
#     channel.basic_consume(queue='stats_queue', on_message_callback=callback)

#     channel.start_consuming()


@shared_task
def consume(request):
    serializer = RecordedGameSerializer(data=request)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print(request)
    print(serializer)
    return 'OK'
