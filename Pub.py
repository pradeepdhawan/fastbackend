import mock

class MockQueuePublisher(QueuePublisher):
    def __init__(self, instance_name, solace_properties):
        self.mock_publisher = mock.create_autospec(QueuePublisher)
        self.guaranteed_publisher = mock.MagicMock()
        self.messaging_service = mock.create_autospec(MessagingService)

class MockMessagingService:
    def __init__(self):
        self.mock_service = mock.create_autospec(MessagingService)
        self.mock_service.create_persistent_message_publisher_builder.return_value = self.mock_publisher

class MockPublishReceipt:
    def __init__(self):
        self.mock_receipt = mock.create_autospec(PublishReceipt)
        self.mock_receipt.message = "sample message"
        self.mock_receipt.is_persisted = True
        self.mock_receipt.time_stamp = datetime.now()
        self.mock_receipt.exception = None

