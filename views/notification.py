from django_socketio.events import on_message


@on_message(channel='notification')
def newTaskNotification(request, socket, context, message):
    # Socket io function: broadcast new added task id
    data = {
        "id": int(message['id'])
    }
    socket.broadcast_channel(data)
