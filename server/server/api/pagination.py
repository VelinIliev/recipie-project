from rest_framework.pagination import PageNumberPagination


class RecipiesPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'size'
    max_page_size = 20
