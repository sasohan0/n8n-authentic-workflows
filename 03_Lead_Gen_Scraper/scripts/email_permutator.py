import sys
import dns.resolver
import json

def generate_emails(first, last, domain):
    emails = []
    f = first.lower()
    l = last.lower()
    
    # Common Corporate Email Formats
    formats = [
        f"{f}.{l}@{domain}",       # john.doe@
        f"{f}@{domain}",           # john@
        f"{f}{l}@{domain}",        # johndoe@
        f"{f[0]}.{l}@{domain}",    # j.doe@
        f"{f}_{l}@{domain}",       # john_doe@
        f"{l}.{f}@{domain}",       # doe.john@
        f"{f[0]}{l}@{domain}",     # jdoe@
        f"{f}{l[0]}@{domain}",     # johnd@
        f"{f[0]}{l[0]}@{domain}",  # jd@
    ]
    return formats

def check_mx_record(domain):
    try:
        # Query for MX records
        records = dns.resolver.resolve(domain, 'MX')
        # Return the highest priority mail server
        mx_record = str(records[0].exchange)
        return True, mx_record
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        return False, None
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    # Expecting args: first_name last_name domain
    if len(sys.argv) < 4:
        print(json.dumps({"error": "Missing arguments"}))
        sys.exit(1)

    first_name = sys.argv[1]
    last_name = sys.argv[2]
    domain = sys.argv[3]

    # 1. Check if Domain is Valid (MX Check)
    is_valid_domain, mx_info = check_mx_record(domain)
    
    # 2. Generate Permutations
    candidates = generate_emails(first_name, last_name, domain)

    # 3. Output JSON
    result = {
        "employee": f"{first_name} {last_name}",
        "domain_status": "Valid" if is_valid_domain else "Invalid/No Email",
        "mx_record": mx_info,
        "email_candidates": candidates[:5], # Return top 5 most likely
        "all_permutations": candidates
    }
    
    # Print JSON to stdout so n8n can read it
    print(json.dumps(result))