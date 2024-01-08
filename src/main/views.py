from flask import Blueprint, render_template
from git import Repo

from . import csrf, services
from .models import Post

main = Blueprint("main", __name__, static_folder="static")


@main.route("/")
def index():
    posts = services.get_all_filter_by(Post, is_public=True)

    return render_template("index.html", posts=posts)


@main.route("/git-update", methods=["POST"])
@csrf.exempt
def git_update():
    repo = Repo("~/Flask-Blog-Project")
    origin = repo.remotes.origin

    # Check out to the 'main' branch (assumed that 'main' is the branch name)
    repo.heads.main.checkout()

    # Pull the latest changes from the origin
    origin.pull()

    # Return a success response
    return "", 200
