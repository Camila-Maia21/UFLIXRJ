from flask import Blueprint
from app.criar_video.controllers import (VideoDetails, VideoCreate)

video_api = Blueprint('/video', __name__)

video_api.add_url_rule(
    '/video', view_func = VideoDetails.as_view('video_details'), methods = ['GET']
)

video_api.add_url_rule(
    '/video/create', view_func = VideoCreate.as_view('video_create'), methods = ['GET', 'POST']
)