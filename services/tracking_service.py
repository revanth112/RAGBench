import uuid


class TrackingService:

    @staticmethod
    def generate_run_id():

        return str(
            uuid.uuid4()
        )