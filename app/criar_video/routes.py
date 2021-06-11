from flask import Blueprint
from app.criar_video.controllers import (VideoCreate, VideoDetails)

video_api = Blueprint('/video', __name__)

video_api.add_url_rule(
    '/video/<int:id>', view_func = VideoDetails.as_view('video_details'), methods = ['GET']
)


video_api.add_url_rule(
    '/video/create/<int:materia_id>', view_func = VideoCreate.as_view('video_create'), methods = ['GET', 'POST']
)
