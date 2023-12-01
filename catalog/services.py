from django.core.cache import cache

def cache_product_view(view_func, timeout=60):
    def cached_view(request, *args, **kwargs):
        cache_key = f'product_view_{kwargs["pk"]}'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return cached_data
        else:
            response = view_func(request, *args, **kwargs)
            cache.set(cache_key, response, timeout)
            return response

    return cached_view
