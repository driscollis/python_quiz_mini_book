# 04_language_looping_spy.py

languages = ["Java", "C++", "Python", "JavaScript", "Julia", "Rust"]
index = 0
for language in languages:
    print(languages)
    print(f"{index = } {language = }")
    languages.remove(language)
    index += 1

print(languages)