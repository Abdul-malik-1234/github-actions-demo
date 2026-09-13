import cgi

def main():
    # Use cgi.escape (a classic utility removed in 3.13)
    text = "<script>alert('hello')</script>"
    escaped_text = cgi.escape(text)
    print(f"Escaped output: {escaped_text}")

if __name__ == "__main__":
    main()
