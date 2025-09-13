from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    # Sets the default page size for this specific paginator
    page_size = 1

    # Allows the client to override the page size using a query parameter
    # e.g., /?page_size=10
    page_size_query_param = 'page_size'

    # Sets a maximum page size to prevent clients from requesting too much data
    max_page_size = 5

    # Allows the client to use a different query parameter for the page number
    # e.g., /?Page-Num=2 instead of /?page=2
    page_query_param = 'Page-Num'

    # The video also shows how to override the response format, but this is optional.
    # The default format is usually sufficient.
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })
