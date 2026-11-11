import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from app.core.similarity import compare_with_label, batch_compare, classify
from app.config import (
    APP_TITLE,
    APP_ICON,
    SAMPLE_DATA_PATH,
    SIMILARITY_THRESHOLD_DUPLICATE,
    SIMILARITY_THRESHOLD_SIMILAR,
)

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Session state for history
# ---------------------------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("### Similarity Thresholds")
st.sidebar.info(f"Duplicate ≥ {SIMILARITY_THRESHOLD_DUPLICATE}")
st.sidebar.info(f"Similar ≥ {SIMILARITY_THRESHOLD_SIMILAR}")
st.sidebar.info(f"Different < {SIMILARITY_THRESHOLD_SIMILAR}")

st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared!")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title(f"{APP_ICON} {APP_TITLE}")
st.markdown(
    "Enter two sentences or questions below to check how similar they are. "
    "The system uses **TF-IDF vectorization** and **Cosine Similarity**."
)

# ---------------------------------------------------------------------------
# Main input area
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    text1 = st.text_area(
        "Text 1",
        placeholder="Enter first sentence or question...",
        height=150,
        key="text1",
    )

with col2:
    text2 = st.text_area(
        "Text 2",
        placeholder="Enter second sentence or question...",
        height=150,
        key="text2",
    )

compare_btn = st.button("🔍 Compare Texts", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Comparison result
# ---------------------------------------------------------------------------
if compare_btn:
    if not text1.strip() or not text2.strip():
        st.warning("⚠️ Please enter both texts before comparing.")
    else:
        score, label = compare_with_label(text1, text2)

        # Save to history
        st.session_state.history.insert(
            0, {"text1": text1, "text2": text2, "score": score, "label": label}
        )
        # Keep only last 10 entries
        st.session_state.history = st.session_state.history[:10]

        # Display result
        st.markdown("---")
        st.subheader("📊 Result")

        result_col1, result_col2, result_col3 = st.columns(3)
        with result_col1:
            st.metric("Similarity Score", f"{score * 100:.2f}%")
        with result_col2:
            label_color = {
                "Duplicate": "🔴",
                "Similar": "🟡",
                "Different": "🟢",
            }.get(label, "⚪")
            st.metric("Classification", f"{label_color} {label}")
        with result_col3:
            st.metric("Text 1 Length", f"{len(text1)} chars")
            st.metric("Text 2 Length", f"{len(text2)} chars")

        # Similarity bar
        st.markdown("### Similarity Visualization")
        fig, ax = plt.subplots(figsize=(6, 1))
        ax.barh([0], [score], color="#4CAF50" if score < 0.5 else "#FFC107" if score < 0.8 else "#F44336")
        ax.set_xlim(0, 1)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        st.pyplot(fig)

# ---------------------------------------------------------------------------
# Batch comparison with sample dataset
# ---------------------------------------------------------------------------
st.markdown("---")
st.subheader("📁 Batch Compare Against Sample Questions")

try:
    if SAMPLE_DATA_PATH.exists():
        df = pd.read_csv(SAMPLE_DATA_PATH)
        if "question" in df.columns:
            reference = st.text_input(
                "Reference question",
                placeholder="Type a question to find similar ones in the dataset...",
            )
            if st.button("Find Similar Questions") and reference.strip():
                candidates = df["question"].dropna().tolist()
                results = batch_compare(reference, candidates)
                st.markdown("### Top Matches")
                res_df = pd.DataFrame(results)
                st.dataframe(res_df, use_container_width=True, hide_index=True)

                # Bar chart of top scores
                top = res_df.head(10)
                fig2, ax2 = plt.subplots(figsize=(8, 4))
                colors = [
                    "#F44336" if s >= SIMILARITY_THRESHOLD_DUPLICATE
                    else "#FFC107" if s >= SIMILARITY_THRESHOLD_SIMILAR
                    else "#4CAF50"
                    for s in top["score"]
                ]
                ax2.barh(top["candidate"], top["score"], color=colors)
                ax2.set_xlabel("Similarity Score")
                ax2.invert_yaxis()
                ax2.set_title("Top 10 Similar Questions")
                st.pyplot(fig2)
    else:
        st.info("Sample dataset not found. Add `data/sample_questions.csv` to enable batch comparison.")
except Exception as e:
    st.error(f"Error loading sample data: {e}")

# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------
if st.session_state.history:
    st.markdown("---")
    st.subheader("🕒 Recent Comparisons")
    for i, entry in enumerate(st.session_state.history):
        with st.expander(f"Comparison {i + 1} — {entry['label']} ({entry['score']*100:.2f}%)"):
            st.write(f"**Text 1:** {entry['text1']}")
            st.write(f"**Text 2:** {entry['text2']}")
            st.write(f"**Score:** {entry['score']*100:.2f}%")
            st.write(f"**Label:** {entry['label']}")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8rem;'>"
    "Built with Python, NLTK, scikit-learn & Streamlit • "
    "Text Similarity & Duplicate Detection Capstone Project"
    "</div>",
    unsafe_allow_html=True,
)
