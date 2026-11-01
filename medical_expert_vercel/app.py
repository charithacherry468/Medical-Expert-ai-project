"""
Back end (Flask) for the Medical Expert Diagnosis System.
Run:  python app.py      then open http://127.0.0.1:5000

Pages:
  /          opening page (heading + choose language)
  /check     enter symptoms (pick from list or type / speak)
  /analyze   reads the form, then redirects to /result
  /result    result page in the chosen language
"""
from flask import Flask, redirect, render_template, request, url_for

import engine
import matcher
import translations as T

app = Flask(__name__, static_folder="public", static_url_path="")


def clean_lang(code):
    return code if code in T.LANGUAGES else "en"


def valid_ids(ids):
    """Keep only known symptom ids, without duplicates."""
    known = set(engine.all_symptoms())
    seen = []
    for i in ids:
        if i in known and i not in seen:
            seen.append(i)
    return seen


def switcher(endpoint, current, **params):
    """Links for the language pills in the header."""
    return [
        {
            "code": code,
            "native": info["native"],
            "active": code == current,
            "url": url_for(endpoint, lang=code, **params),
        }
        for code, info in T.LANGUAGES.items()
    ]


@app.route("/")
def index():
    return render_template("index.html", lang="en", languages=T.LANGUAGES)


@app.route("/check")
def check():
    lang = clean_lang(request.args.get("lang"))
    symptoms = [
        {
            "id": sid,
            "name": T.sname(sid, lang),
            "emoji": T.SYMPTOM_EMOJI[sid],
            "severe": sid in engine.SEVERE,
            "search": T.search_text(sid),
        }
        for sid in T.SYMPTOM_ORDER
    ]
    return render_template(
        "check.html",
        lang=lang,
        t=T.UI[lang],
        symptoms=symptoms,
        speech=T.LANGUAGES[lang]["speech"],
        text=request.args.get("text", "")[:300],
        error=request.args.get("err") == "1",
        unknown=request.args.getlist("u")[:5],
        switch=switcher("check", lang),
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    lang = clean_lang(request.form.get("lang"))
    text = request.form.get("text", "")[:300]

    picked = request.form.getlist("symptoms")
    typed, unknown = matcher.parse(text)
    ids = valid_ids(picked + typed)
    unknown = unknown[:5]

    if not ids:
        return redirect(url_for("check", lang=lang, err=1, u=unknown, text=text))
    return redirect(url_for("result", lang=lang, s=ids, u=unknown))


@app.route("/result")
def result():
    lang = clean_lang(request.args.get("lang"))
    ids = valid_ids(request.args.getlist("s"))
    if not ids:
        return redirect(url_for("check", lang=lang, err=1))

    out = engine.run(ids)

    cards = []
    for rank, r in enumerate(out["results"], start=1):
        d = T.DISEASES[r["id"]]
        cards.append({
            "rank": rank,
            "emoji": d["emoji"],
            "name": d[lang]["name"],
            "advice": d[lang]["advice"],
            "matched": [T.sname(s, lang) for s in r["matched"]],
            "count": r["count"],
            "total": r["total"],
            "pct": round(100 * r["count"] / r["total"]),
        })

    ruled = [
        {
            "name": T.DISEASES[x["id"]][lang]["name"],
            "because": [T.sname(s, lang) for s in x["because"]],
        }
        for x in out["ruled_out"]
    ]

    chosen = [
        {
            "name": T.sname(s, lang),
            "emoji": T.SYMPTOM_EMOJI[s],
            "severe": s in engine.SEVERE,
        }
        for s in ids
    ]

    return render_template(
        "result.html",
        lang=lang,
        t=T.UI[lang],
        cards=cards,
        ruled=ruled,
        chosen=chosen,
        warning=out["warning"],
        unknown=request.args.getlist("u")[:5],
        switch=switcher("result", lang, s=ids),
    )


if __name__ == "__main__":
    app.run(debug=True)
