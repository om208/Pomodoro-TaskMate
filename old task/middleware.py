from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Exception occurred: {exception}")
        return None