"""Posts service"""

import logging

logger = logging.getLogger(__name__)


class PostsService:
    """Service for posts operations"""
    
    async def get_posts(self, platform, limit, offset):
        """Get posts from social media"""
        try:
            logger.info(f"Getting posts from platform: {platform}")
            return []
        except Exception as e:
            logger.error(f"Error getting posts: {str(e)}")
            raise
    
    async def get_post(self, post_id):
        """Get specific post"""
        try:
            logger.info(f"Getting post: {post_id}")
            return None
        except Exception as e:
            logger.error(f"Error getting post: {str(e)}")
            raise
