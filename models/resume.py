import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from werkzeug.utils import secure_filename

from services.pdf_extractor import extract_text_from_pdf


resume_bp = Blueprint("resume", __name__)


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


@resume_bp.route("/")
def home():

    return render_template("index.html")


@resume_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "GET":

        return render_template("upload.html")

    resume = request.files.get("resume")

    career_goal = request.form.get("career_goal", "").strip()

    if not resume:

        flash("Please upload your resume.")

        return redirect(url_for("resume.upload"))

    if resume.filename == "":

        flash("Please select a PDF file.")

        return redirect(url_for("resume.upload"))

    if not allowed_file(resume.filename):

        flash("Only PDF files are allowed.")

        return redirect(url_for("resume.upload"))

    if not career_goal:

        flash("Please enter your career goal.")

        return redirect(url_for("resume.upload"))

    filename = secure_filename(resume.filename)

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    resume.save(filepath)

    try:

        resume_text = extract_text_from_pdf(filepath)

        if not resume_text.strip():

            flash("Could not extract text from the PDF.")

            return redirect(url_for("resume.upload"))

    except Exception as e:

        print("PDF ERROR:", e)

        flash("Could not read the PDF.")

        return redirect(url_for("resume.upload"))

    return redirect(
        url_for(
            "analysis.analyze",
            resume_text=resume_text,
            career_goal=career_goal
        )
    )