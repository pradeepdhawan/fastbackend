class PersistentMessageReceiver:
    def __init__(self, messaging_service, queue_name):
        self.messaging_service = messaging_service
        self.queue_name = queue_name
        self.on_message_received = None
        self.on_message_failed = None

    def start(self):
        print("PersistentMessageReceiver: start")

    def stop(self):
        print("PersistentMessageReceiver: stop")

    def ack(self, message):
        print("PersistentMessageReceiver: ack")
        
    def set_on_message_received_callback(self, callback):
        self.on_message_received = callback
        
    def set_on_message_failed_callback(self, callback):
        self.on_message_failed = callback
    
    def mock_receive_message(self, payload, properties=None, application_id=None, correlation_id=None):
        if self.on_message_received:
            self.on_message_received(payload, properties, application_id, correlation_id)
            
    def mock_receive_failed_message(self, payload, error):
        if self.on_message_failed:
            self.on_message_failed(payload, error)
