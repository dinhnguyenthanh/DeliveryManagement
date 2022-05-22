from rest_framework import pagination


class CategoryItemPaginator(pagination.PageNumberPagination):
    page_size = 6
