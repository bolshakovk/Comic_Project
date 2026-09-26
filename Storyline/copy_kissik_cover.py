import shutil

src = r"C:\Users\bolsh\.gemini\antigravity\brain\f37350dd-ff5c-44d4-9cb5-8ae597270cbe\kissik_vanderheim_cover_1787769572994.png"
dst = r"c:\Users\bolsh\OneDrive\Документы\saga of black diamond\Comic_Project\Storyline\kissik_cover.png"

shutil.copyfile(src, dst)
print("Copied Kissik cover successfully!")
