from django.core.paginator import Paginator


POSTS_PER_PAGE: int = 10


def paginate(posts, request):
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)
