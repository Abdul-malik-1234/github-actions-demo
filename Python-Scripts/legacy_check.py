import cgi

def main():
    # cgi.parse_header exists in 3.12, but 'cgi' as a whole is removed in 3.13
    header_val, params = cgi.parse_header("text/html; charset=utf-8")
    print(f"Content Type: {header_val}")

if __name__ == "__main__":
    main()
