def reverse(swapthis):
    rethis = {}
    for _ in swapthis:
        rethis[swapthis[_]] = _
    return rethis

def keys(source, check):
    repeated_value = []
    for _ in source:
        if source[_] == check:
            repeated_value.append(_)
    return repeated_value

exec(input().strip())
