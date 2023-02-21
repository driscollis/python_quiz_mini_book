# 04_language_looping.py

languages = ["Java", "C++", "Python", "JavaScript", "Julia", "Rust"]
for language in languages:
    languages.remove(language)
    
print(languages)