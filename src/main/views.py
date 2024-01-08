from flask import Blueprint, render_template

from . import services
from .models import Post

main = Blueprint("main", __name__, static_folder="static")


@main.route("/")
def index():
    posts = services.get_all_filter_by(Post, is_public=True)

    return render_template("index.html", posts=posts)


# @main.route("/git-update", methods=["POST"])
# @csrf.exempt
# def git_update():
#     repo = git.Repo("./Flask-Blog-Project")
#     origin = repo.remotes.origin
#     repo.create("main", origin.refs.main).set_tracking_branch(
#         origin.refs.main
#     ).checkout()
#     origin.pull()
#     return "", 200
