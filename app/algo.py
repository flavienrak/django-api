from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
import numpy as np


# Dictionnaire de synonymes
synonyms = {
    "développeur web": ["ingénieur web", "programmeur web", "webmaster"],
    "analyste financier": ["expert comptable", "auditeur financier"],
    # Ajoutez d'autres synonymes
}


def expand_synonyms(terms):
    expanded_terms = []
    for term in terms:
        expanded_terms.extend(synonyms.get(term, [term]))
    return expanded_terms


def compute_similarity(job, profile):
    fields = [
        "competences",
        "experiences",
        "formations",
        "langues",
        "qualites",
        "diplomes",
    ]
    weights = {
        "titre": 0.2,
        "competences": 0.3,
        "experiences": 0.15,
        "formations": 0.1,
        "langues": 0.075,
        "qualites": 0.075,
        "diplomes": 0.1,
    }

    similarities = {}

    # Comparaison des titres avec les postes recherchés par l'utilisateur
    titre_similarities = []
    for titre_recherche in profile.postes:
        max_similarity = 0
        for synonym in expand_synonyms([titre_recherche]):
            similarity = fuzz.token_set_ratio(job.titre, synonym) / 100.0
            max_similarity = max(max_similarity, similarity)
        titre_similarities.append(max_similarity)
    similarities["titre"] = np.mean(titre_similarities) if titre_similarities else 0

    for field in fields:
        job_desc = getattr(job, field, [])
        profile_desc = getattr(profile, field, [])

        job_desc_str = " ".join(job_desc)
        profile_desc_str = " ".join(profile_desc)

        if not job_desc_str or not profile_desc_str:
            similarities[field] = 0

        else:
            vectorizer = TfidfVectorizer(stop_words=None, min_df=1, max_df=1.0)

            tfidf_job = vectorizer.fit_transform([job_desc_str])
            tfidf_profile = vectorizer.transform([profile_desc_str])

            similarity = cosine_similarity(tfidf_profile, tfidf_job)[0][0]
            similarities[field] = similarity

    global_score = sum(weights[field] * similarities[field] for field in fields)
    return {"details": similarities, "global_score": global_score}
