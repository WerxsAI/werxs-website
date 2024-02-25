from datetime import datetime
from flask import current_app as app
from bson.objectid import ObjectId  # For ObjectId to work


class BlogModel:
    def __init__(self, db):
        self.collection = db.blogPosts

    def find_blog_post(self, blog_id):
        return self.collection.find_one({"_id": ObjectId(blog_id)})

    def create_blog_post(
        self, title, author, content, category_name, image_url, likes=0, page_views=0
    ):
        blog_post = {
            "title": title,
            "author": author,
            "content": content,
            "category_name": category_name,
            "image_url": image_url,
            "date_posted": datetime.utcnow(),
            "likes": likes,
            "page_views": page_views,
        }
        result = self.collection.insert_one(blog_post)
        app.logger.info("Blog post created with id: %s", result.inserted_id)
        return result.inserted_id

    def update_blog_post(self, blog_id, update_data):
        result = self.collection.update_one(
            {"_id": ObjectId(blog_id)}, {"$set": update_data}
        )
        app.logger.info(
            "Updated blog post: %s, Update Result: %s", blog_id, result.modified_count
        )
        return result.modified_count

    def delete_blog_post(self, blog_id):
        result = self.collection.delete_one({"_id": ObjectId(blog_id)})
        app.logger.info(
            "Deleted blog post: %s, Delete Result: %s", blog_id, result.deleted_count
        )
        return result.deleted_count

    def search_blog_posts(self, search_str):
        # Assuming a text index has been created on the fields you want to search
        result = self.collection.find(
            {"$text": {"$search": search_str}}, {"slug": 1, "description": 1}
        ).limit(10)
        return list(result)
