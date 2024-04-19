import json
import os

def analyze_threat_intelligence(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        # Initialize counters for statistics
        total_cves = 0
        total_xss_vulnerabilities = 0
        total_authentication_bypass_vulnerabilities = 0
        
        # Extract CVEs and analyze relevant threats
        cves = data.get('CVE_Items', [])
        for cve in cves:
            total_cves += 1
            
            # Extract CVE ID
            cve_id = cve.get('cve', {}).get('CVE_data_meta', {}).get('ID', 'N/A')
            
            # Extract description
            description = cve.get('cve', {}).get('description', {}).get('description_data', [{}])[0].get('value', 'N/A')
            
            # Extract references
            references = cve.get('cve', {}).get('references', {}).get('reference_data', [])
            
            # Check if the vulnerability is cross-site scripting (XSS)
            if "cross-site scripting" in description.lower():
                total_xss_vulnerabilities += 1
                
            # Check if the vulnerability enables authentication bypass
            if "authentication bypass" in description.lower():
                total_authentication_bypass_vulnerabilities += 1
                
        # Print statistics
        print("----- Statistics -----")
        print(f"Total CVEs: {total_cves}")
        print(f"Total XSS Vulnerabilities: {total_xss_vulnerabilities}")
        print(f"Total Authentication Bypass Vulnerabilities: {total_authentication_bypass_vulnerabilities}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyze_threat_intelligence.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    analyze_threat_intelligence(file_path)
