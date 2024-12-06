dau = 10_000_000
d = 86400

# posts 
# delete post
post_item_size = 500 + 3 * 36 + 36 + 36
images_in_post = 3

create_post = 3
delete_post = 1/30
retrieve_post = 8
list_posts_by_user_id = 5

create_posts_rps = dau * create_post / d
delete_posts_rps = dau * delete_post / d
retrieve_post_rps = dau * retrieve_post / d
list_posts_by_user_id_rps = dau * list_posts_by_user_id / d

create_like = 8
delete_like = 2

create_like_rps = dau * create_like / d
delete_like_rps = dau * delete_like / d

post_writes_rps = create_posts_rps + delete_posts_rps + create_like_rps + delete_like_rps
post_reads_rps = retrieve_post_rps + list_posts_by_user_id_rps

print("create_post_rps:", create_posts_rps)
print("delete_posts_rps:", delete_posts_rps)
print("retrieve_post_rps:", retrieve_post_rps)
print("list_posts_by_user_id_rps:", list_posts_by_user_id_rps)

print("create_like_rps:", create_like_rps)
print("delete_like_rps:", delete_like_rps)

print("post_writes_rps:", post_writes_rps)
print("post_reads_rps:", post_reads_rps)


# locations
list_top_locations = 5
list_top_locations_rps = list_top_locations * dau / d

locations_read_rps = list_top_locations_rps + retrieve_post_rps

print("list_top_locations_rps:", list_top_locations_rps)
print("locations_read_rps:", locations_read_rps)

# comments
create_comment = 5
delete_comment = 1

create_comment_rps = dau * create_comment / d
delete_comment_rps = dau * delete_comment / d

comments_write_rps = create_comment_rps + delete_comment_rps
comments_read_rps = retrieve_post_rps

print("create_comment_rps:", create_comment_rps)
print("delete_comment_rps:", delete_comment_rps)
print("comments_write_rps:", comments_write_rps)
print("comments_read_rps:", comments_read_rps)

# feed
feed = 13
feed_rps = dau * feed / d

feed_read_rps = feed_rps + 0

print("feed_rps:", feed_rps)
print("feed_read_rps:", feed_read_rps)

# images 
images_max_bytes = 1 * 1024 * 1024
upload_images_rps = create_posts_rps * images_in_post
delete_images_rps = delete_posts_rps * images_in_post

images_read_rps = retrieve_post_rps + list_posts_by_user_id_rps + feed_rps
images_write_rps = upload_images_rps + delete_images_rps

images_write_traffic = upload_images_rps * images_max_bytes
images_read_traffic = images_read_rps * images_max_bytes

print("images_read_rps:", images_read_rps)
print("images_write_rps:", images_write_rps)
print("images_write_traffic:", images_write_traffic / 1024 / 1024)
print("images_read_traffic:", images_read_traffic / 1024 / 1024)

# follows
create_follow = 2
delete_follow = 1

create_follow_rps = create_follow * dau / d
delete_follow_rps = dau * delete_follow / d

follow_writes_rps = create_follow_rps + delete_follow_rps

print("create_follow_rps:", create_follow_rps)
print("delete_follow_rps:", delete_follow_rps)
print("follow_writes_rps:", follow_writes_rps)

total_write_rps = post_writes_rps + comments_write_rps + images_write_rps + follow_writes_rps
total_read_rps = post_reads_rps + comments_read_rps + feed_read_rps + images_read_rps

print("total_write_rps:", total_write_rps)
print("total_read_rps:", total_read_rps)
