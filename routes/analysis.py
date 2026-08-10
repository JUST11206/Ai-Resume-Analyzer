from flask import Blueprint, render_template, request

from services.ai_analyzer import analyze_resume


# IMPORTANT: name must be analysis_bp
analysis_bp = Blueprint("analysis", __name__)


@analysis_bp.route("/analyze")
def analyze():

    resume_text = request.args.get("resume_text", "")
    career_goal = request.args.get("career_goal", "")

    if not resume_text or not career_goal:
        return "Resume or career goal missing.", 400

    try:

        result = analyze_resume(
            resume_text,
            career_goal
        )

        return render_template(
            "result.html",
            result=result
        )

    except Exception as e:

        print("AI ERROR:", e)

        return f"""
        <h2>AI Analysis Failed</h2>
        <p>{str(e)}</p>
        """, 500