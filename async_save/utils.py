from pprint import pprint
from celery import shared_task


@shared_task
def save_file(instance):
    file_data = file_field
    total_size = instance.size
    chunk_size = 65536
    # Number of iteration
    chunks = total_size / chunk_size + 1
    for chunk in file_data.chunks():
        chunks -= 1
        instance.percents = chunks
        instance.characters += very_simple_parser(chunk)
        instance.save()

    instance.ready = True
    instance.save()


def very_simple_parser(text):
    text = text.replace(' ', '')
    return len(text)
