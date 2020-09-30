def pod(total, podcasts):
    podcast_len = {}
​
    for p in podcasts:
        podcast_len[p] = True
​
    """
    # Set version equivalent to dict, above
    podcast_len = set()
​
    for p in podcasts:
        podcast_len.add(p)
    """
​
    for p0 in podcasts:
        other_podcast_len = total - p0
        # is there a podcast of total - p0 minutes?
        if other_podcast_len in podcast_len:
            return True
​
    return False
​
​
"""
total == 60
p0 == 27
p1 == 60 - 27 == total - p0 == 33
"""
