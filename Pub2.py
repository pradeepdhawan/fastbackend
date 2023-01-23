import mock

class MockTopicPublisher(TopicPublisher):
    def __init__(self, instance_name, solace_properties):
        self.mock_publisher = mock.create_autospec(TopicPublisher)
        self.direct_publisher = mock.MagicMock()
        self.messaging_service = mock.create_autospec(MessagingService)

class MockMessagingService:
    def __init__(self):
        self.mock_service = mock.create_autospec(MessagingService)
        self.mock_service.create_direct_message_publisher_builder.return_value = self.mock_publisher

class MockFailedPublishEvent:
    def __init__(self):
        self.mock_event = mock.create_autospec(FailedPublishEvent)
        self.mock_event.get_cause = mock.MagicMock(return_value="sample cause")
