dau = 10_000_000
d = 86400

# auth
sign_up = dau / 365

# posts
create_post = 1
delete_post = 1/30
retrieve_post = 10
list_posts_by_user_id = 5
likes = 8
dislikes = 2
images_per_post = 3
find_location_per_post = 5

# feed
list_feed = 13 # (20 items per page)

# images
images_upload = create_post * images_per_post
images_download = retrieve_post * images_per_post + list_feed * 20

# comments
list_comments = retrieve_post * 2 # 2 pages
create_comment = 3
delete_comment = 1

# follow
follow = 2
unfollow = 1

# locations
locations_with_posts = 5
list_locations = create_post * find_location_per_post

def auth_metrics():
    return {
        "sign_up": sign_up / d,
    }

def post_metrics():
    dct = {
        "create_post": create_post * dau / d,
        "delete_post": delete_post * dau / d,
        "retrieve_post": retrieve_post * dau / d,
        "list_posts_by_user_id": list_posts_by_user_id * dau / d,
        "likes": likes * dau / d,
        "dislikes": dislikes * dau / d,
        "list_feed": list_feed * dau / d,
    }
    dct.update({
        "post_writes": dct["create_post"] + dct["delete_post"] + dct["likes"] + dct["dislikes"],
        "post_reads": dct["retrieve_post"] + dct["list_posts_by_user_id"] + dct["list_feed"],
    })
    return dct

def images_metrics():
    dct = {
        "images_upload": images_upload * dau / d,
        "images_download": images_download * dau / d,
    }
    return dct

def comments_metrics():
    dct = {
        "create_comment": create_comment * dau / d,
        "delete_comment": delete_comment * dau / d,
        "list_comments": list_comments * dau / d,
    }
    dct.update({
        "comments_writes": dct["create_comment"] + dct["delete_comment"],
        "comments_reads": dct["list_comments"],
    })

    return dct


def follow_metrics():
    return {
        "follow": follow * dau / d,
        "unfollow": unfollow * dau / d,
    }

def locations_metrics():
    dct = {
        "locations_with_posts": locations_with_posts * dau / d,
        "list_locations": list_locations * dau / d,
    }
    dct.update({
        "locations_reads": dct["list_locations"] + dct["locations_with_posts"],
    })
    return dct

posts = post_metrics()
images = images_metrics()
comments = comments_metrics()
follow = follow_metrics()
locations = locations_metrics()
auth = auth_metrics()

total_read = posts["post_reads"] + images["images_download"] + comments["comments_reads"] + locations["locations_reads"]
total_write = posts["post_writes"] + images["images_upload"] + comments["comments_writes"] + follow["follow"] + auth["sign_up"]

r = {

    "auth": auth,
    "posts": posts,
    "images": images,
    "comments": comments,
    "follow": follow,
    "locations": locations,
}
print("total_read:", total_read)
print("total_write:", total_write)

for k, v in r.items():
    print(f"{k}:")
    for kk, vv in v.items():
        print(f"\t{kk}: {vv:.2f}")
