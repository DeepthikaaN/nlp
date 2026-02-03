import re

text = """Hello Team 👋🚀
 #Product Launch, @world, @world We're excited to build the future together! 💡✨ Follow us on social media 📲 to stay updated with our latest launches, offers, and growth stories 📈🔥
Our starter plan begins at just $99 💰 — simple, powerful, and built to scale 🚀💼
📧 Reach us anytime at hello@startup.io
"""

# 1. Hashtags: Look for # followed by word characters
hashtags = re.findall(r"#\w+", text)

# 2. Mentions: Look for @ followed by word characters (set() removes duplicates)
mentions = list(set(re.findall(r"@\w+", text)))

# 3. Emails: Basic pattern for username@domain.extension
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

# 4. URLs: Look for http/https (Note: none in your current text, but pattern is ready)
urls = re.findall(r"https?://\S+", text)

# 5. Prices: Added this since your text has '$99'
prices = re.findall(r"\$\d+", text)

# 6. Tokens: Extracting all individual words
tokens = re.findall(r"\b\w+\b", text)

print("Hashtags:", hashtags)
print("Mentions:", mentions)
print("Emails:", emails)
print("Prices:", prices)
print("Tokens (first 5):", tokens[:5])
