# 📸 Screenshots Section

Ye folder project ke running app ke screenshots ke liye hai.

## 📋 Kon-se screenshots daalne hain

Har member apne module ke liye ek screenshot daale:

| Member | File | Kya capture karein |
|--------|------|-------------------|
| Anirudh Core | `member1_preprocessing.png` | Preprocessing notebook output |
| Aaditya Core | `member2_similarity.png` | Similarity calculation output |
| Anshuman Core | `member3_streamlit_ui.png` | Streamlit app running in browser |

## 🚀 App kaise run karein screenshot ke liye

```powershell
# Terminal mein
cd C:\Users\ABHISHEK\Desktop\Nlp Project
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/ui/streamlit_app.py
```

Browser mein `http://localhost:8501` khulega — wahan se screenshot lein.

## 📁 Folder Structure

```text
screenshots/
├── README.md              # Ye file
├── member1_preprocessing.png  # Anirudh ka screenshot
├── member2_similarity.png     # Aaditya ka screenshot
└── member3_streamlit_ui.png   # Anshuman ka screenshot
```

## 📤 Kaise upload karein GitHub pe

1. Apne computer pe screenshot lein (`.png` ya `.jpg`)
2. Is folder mein copy karein
3. Git commit aur push karein:
   ```powershell
   git add screenshots/
   git commit -m "Add screenshots for project demo"
   git push origin main
   ```

---

## ✅ Current Status

| Screenshot | Status |
|------------|--------|
| Member 1 (Preprocessing) | ⏳ Pending |
| Member 2 (Similarity) | ⏳ Pending |
| Member 3 (Streamlit UI) | ⏳ Pending |

Teeno members apne-apne screenshots yahan daalein jab app ready ho jaye.
