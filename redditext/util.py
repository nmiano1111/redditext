

def print_yaml(sfw_sub_cache, nsfw_sub_cache):
    print("sfw:")
    for s in sfw_sub_cache:
        print(f'  - {s}')

    print("nsfw:")
    for n in nsfw_sub_cache:
        print(f'  - {n}')


# TODO: clean up
def process_url(post):
    if 'www.reddit.com' in post['url'] or\
            'v.redd.it' in post['url'] or\
            'youtu' in post['url'] or\
            'preview.redd.it' in post['url'] or\
            '/r/' in post['url']:
        url = f'https://www.redditmedia.com{post["permalink"]}?ref_source=embed&amp;ref=share&amp;embed=true&amp;theme=dark'
    else:
        url = post['url']

    return url






