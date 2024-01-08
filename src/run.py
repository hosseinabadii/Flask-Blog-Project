from git import Repo

from main import create_app, csrf

app = create_app()


@app.route("/git-update", methods=["POST"])
@csrf.exempt
def git_update():
    repo = Repo("./Flask-Blog-Project")
    origin = repo.remotes.origin

    # Check out to the 'main' branch (assumed that 'main' is the branch name)
    repo.heads.main.checkout()

    # Pull the latest changes from the origin
    origin.pull()

    # Return a success response
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
