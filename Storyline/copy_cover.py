import shutil

src = r"C:\Users\bolsh\.gemini\antigravity\brain\f37350dd-ff5c-44d4-9cb5-8ae597270cbe\valheim_song_cover_1787768917401.png"
dst = r"c:\Users\bolsh\OneDrive\Документы\saga of black diamond\Comic_Project\Storyline\valheim_cover.png"

shutil.copyfile(src, dst)
print("Copied cover image successfully!")
