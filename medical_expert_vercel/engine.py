"""
Inference engine for the Medical Expert Diagnosis System.
AI experiments: Knowledge Base, Unification, Default Reasoning
Educational prototype only. Not a medical tool.
"""

# ------------------------------------------------------------
# 1. KNOWLEDGE BASE
# ------------------------------------------------------------
KB = [
    ("symptom", "common_cold", "sneezing"),
    ("symptom", "common_cold", "runny_nose"),
    ("symptom", "common_cold", "sore_throat"),
    ("symptom", "common_cold", "cough"),

    ("symptom", "flu", "fever"),
    ("symptom", "flu", "cough"),
    ("symptom", "flu", "body_ache"),
    ("symptom", "flu", "headache"),
    ("symptom", "flu", "fatigue"),
    ("symptom", "flu", "sore_throat"),

    ("symptom", "malaria", "high_fever"),
    ("symptom", "malaria", "chills"),
    ("symptom", "malaria", "sweating"),
    ("symptom", "malaria", "headache"),
    ("symptom", "malaria", "nausea"),
    ("symptom", "malaria", "fatigue"),

    ("symptom", "dengue", "high_fever"),
    ("symptom", "dengue", "headache"),
    ("symptom", "dengue", "joint_pain"),
    ("symptom", "dengue", "eye_pain"),
    ("symptom", "dengue", "rash"),

    ("symptom", "typhoid", "high_fever"),
    ("symptom", "typhoid", "abdominal_pain"),
    ("symptom", "typhoid", "headache"),
    ("symptom", "typhoid", "loss_of_appetite"),
    ("symptom", "typhoid", "constipation"),
    ("symptom", "typhoid", "fatigue"),

    ("symptom", "gastroenteritis", "vomiting"),
    ("symptom", "gastroenteritis", "diarrhea"),
    ("symptom", "gastroenteritis", "abdominal_pain"),
    ("symptom", "gastroenteritis", "nausea"),
    ("symptom", "gastroenteritis", "fever"),
]

# General advice only (no dosages)
TREATMENT = {
    "common_cold": "Rest, warm fluids, steam inhalation.",
    "flu": "Rest, plenty of fluids, fever relief as advised by a doctor.",
    "malaria": "Needs a blood test and prescribed medicine. See a doctor.",
    "dengue": "Needs a blood test. Rest and fluids; see a doctor for monitoring.",
    "typhoid": "Needs a lab test and prescribed antibiotics. See a doctor.",
    "gastroenteritis": "Oral rehydration, light food; see a doctor if it lasts long.",
}

# Warning signs that need urgent medical attention
SEVERE = {"breathing_difficulty", "chest_pain", "confusion"}


# ------------------------------------------------------------
# 2. UNIFICATION
# A variable is a string starting with "?".
#   unify(("symptom", "?D", "rash"), ("symptom", "dengue", "rash"))
#   -> {"?D": "dengue"}
# ------------------------------------------------------------
def is_var(x):
    return isinstance(x, str) and x.startswith("?")


def unify(pattern, fact, bindings=None):
    if len(pattern) != len(fact):
        return None
    b = dict(bindings or {})
    for p, f in zip(pattern, fact):
        if is_var(p):
            if p in b and b[p] != f:
                return None
            b[p] = f
        elif p != f:
            return None
    return b


def query(pattern):
    """Return the bindings for every fact in the KB that unifies."""
    results = []
    for fact in KB:
        b = unify(pattern, fact)
        if b is not None:
            results.append(b)
    return results


def diseases():
    return sorted(TREATMENT)


def all_symptoms():
    found = {b["?S"] for b in query(("symptom", "?D", "?S"))}
    return sorted(found | SEVERE)


def matched_symptoms(disease, user_symptoms):
    """Symptoms of `disease` that the user also has (found by unification)."""
    return [s for s in user_symptoms if query(("symptom", disease, s))]


# ------------------------------------------------------------
# 3. DEFAULT REASONING
# Default: a disease is assumed likely if at least 2 of its symptoms
# match, UNLESS an exception applies (then the conclusion is withdrawn).
# ------------------------------------------------------------
EXCEPTIONS = {
    "common_cold": {"high_fever", "breathing_difficulty"},
    "flu": {"rash"},
    "gastroenteritis": {"breathing_difficulty"},
}

MIN_MATCHES = 2


def ruled_out(disease, user_symptoms):
    return bool(EXCEPTIONS.get(disease, set()) & set(user_symptoms))


def total_symptoms(disease):
    return len(query(("symptom", disease, "?S")))


def run(user_symptoms):
    """Full diagnosis. Returns ids only; the web layer translates them."""
    results = []
    excluded = []
    for d in diseases():
        matched = matched_symptoms(d, user_symptoms)
        if len(matched) < MIN_MATCHES:
            continue
        if ruled_out(d, user_symptoms):
            because = [s for s in user_symptoms if s in EXCEPTIONS[d]]
            excluded.append({"id": d, "because": because})
        else:
            results.append({
                "id": d,
                "matched": matched,
                "count": len(matched),
                "total": total_symptoms(d),
            })
    results.sort(key=lambda r: (r["count"], r["count"] / r["total"]), reverse=True)
    return {
        "results": results,
        "ruled_out": excluded,
        "warning": bool(SEVERE & set(user_symptoms)),
    }
