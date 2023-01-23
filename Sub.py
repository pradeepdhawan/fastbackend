class QueueReceiver:
    class ServiceEventHandler:
        def on_reconnected(self, service_event: ServiceEvent):
            print("ServiceEventHandler: on_reconnected")

        def on_reconnecting(self, event: ServiceEvent):
            print("ServiceEventHandler: on_reconnecting")

        def on_service_interrupted(self, event: ServiceEvent):
            print("ServiceEventHandler: on_service_interrupted")

    class QueueMessageHandler:
        def __init__(self, receiver=None, ack=True, source_topic='', on_message_received=None, on_message_failed=None):
            pass

        def on_message(self, message: InboundMessage):
            print("QueueMessageHandler: on_message")
            if self._on_message_received:
                self._on_message_received("dummy payload", "dummy properties", "dummy application_id", "dummy correlation_id")

    def __init__(self, messaging_service, queue_name):
        pass

    def start_receiving(self):
        print("QueueReceiver: start_receiving")

    def stop_receiving(self):
        print("QueueReceiver: stop_receiving")
