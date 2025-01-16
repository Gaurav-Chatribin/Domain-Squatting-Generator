import itertools
import string
import re
import random
import unicodedata
import csv
from datetime import datetime
import os
import socket
import concurrent.futures
import urllib.request
import ssl

class DomainSquatter:
    def __init__(self, domain):
        # Split domain into name and TLD
        self.domain_parts = domain.split('.')
        self.domain_name = self.domain_parts[0]
        self.tld = self.domain_parts[1] if len(self.domain_parts) > 1 else ''
    
    def typosquatting(self):
        """Generate domains with advanced typo techniques."""
        typo_techniques = [
            # Enhanced keyboard proximity and character replacement
            self._advanced_keyboard_adjacent_chars,
            # Repeated characters
            self._repeated_chars,
            # Missed characters
            self._missed_chars,
            # Swapped adjacent characters
            self._swapped_chars,
            # Transposition of characters
            self._transposed_chars,
            # Common character replacements
            self._character_replacements
        ]
        
        typo_domains = []
        for technique in typo_techniques:
            typo_domains.extend(technique())
        
        return [f"{domain}.{self.tld}" for domain in set(typo_domains)]
    
    def _advanced_keyboard_adjacent_chars(self):
        """Generate advanced typos based on keyboard proximity and character similarity."""
        keyboard_map = {
            'q': 'wa1', 'w': 'qase2', 'e': 'wr3', 'r': 'et4', 't': 'ry5',
            'y': 'tu6', 'u': 'yi7', 'i': 'uo8', 'o': 'ip9', 'p': 'o0',
            'a': 'qwsz@', 's': 'adz#', 'd': 'sfc$', 'f': 'dg%', 'g': 'fh^',
            'h': 'gj&', 'j': 'hk*', 'k': 'jl(', 'l': 'k)',
            'z': 'ax', 'x': 'zc', 'c': 'xv', 'v': 'cb', 'b': 'vn', 'n': 'bm', 'm': 'n'
        }
        
        variations = []
        for i in range(len(self.domain_name)):
            if self.domain_name[i] in keyboard_map:
                for adj_char in keyboard_map[self.domain_name[i]]:
                    variation = self.domain_name[:i] + adj_char + self.domain_name[i+1:]
                    variations.append(variation)
        
        return variations
    
    def _transposed_chars(self):
        """Generate domains with transposed characters."""
        variations = []
        for i in range(len(self.domain_name) - 1):
            variation = (
                self.domain_name[:i] + 
                self.domain_name[i+1] + 
                self.domain_name[i] + 
                self.domain_name[i+2:]
            )
            variations.append(variation)
        return variations
    
    def _character_replacements(self):
        """Generate domains with common character replacements."""
        replacement_map = {
            'a': ['4', '@'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['5', '$'],
            't': ['7']
        }
        
        variations = []
        for i, char in enumerate(self.domain_name):
            if char.lower() in replacement_map:
                for replace_char in replacement_map[char.lower()]:
                    variation = self.domain_name[:i] + replace_char + self.domain_name[i+1:]
                    variations.append(variation)
        
        return variations
    
    def _repeated_chars(self):
        """Generate domains with repeated characters."""
        variations = []
        for i in range(len(self.domain_name)):
            variation = self.domain_name[:i] + self.domain_name[i] * 2 + self.domain_name[i+1:]
            variations.append(variation)
        return variations
    
    def _missed_chars(self):
        """Generate domains with missed characters."""
        variations = []
        for i in range(len(self.domain_name)):
            variation = self.domain_name[:i] + self.domain_name[i+1:]
            variations.append(variation)
        return variations
    
    def _swapped_chars(self):
        """Generate domains with swapped adjacent characters."""
        variations = []
        for i in range(len(self.domain_name) - 1):
            variation = (
                self.domain_name[:i] + 
                self.domain_name[i+1] + 
                self.domain_name[i] + 
                self.domain_name[i+2:]
            )
            variations.append(variation)
        return variations
    
    def homograph_attack(self):
        """Generate advanced homograph domains using extensive Unicode characters."""
        homograph_map = {
            'a': ['а', 'ạ', 'ά', 'ä', 'â'],  # Cyrillic, decorated, Greek, German variants
            'c': ['ϲ', 'с', 'ϲ', 'ⅽ'],  # Greek, Cyrillic, special forms
            'e': ['е', 'ё', 'ε', 'ē'],  # Cyrillic, Greek, extended variants
            'o': ['о', '0', 'ο', 'ό', 'ö'],  # Cyrillic, zero, Greek, German
            'p': ['р', 'ρ', 'ϱ'],  # Cyrillic, Greek variants
            's': ['ѕ', 'ꜱ', 'ṡ'],  # Cyrillic, small caps, decorated
            'x': ['х', 'ⅹ', 'ₓ']  # Cyrillic, special forms
        }
        
        variations = [self.domain_name]
        for i, char in enumerate(self.domain_name):
            if char.lower() in homograph_map:
                for alt_char in homograph_map[char.lower()]:
                    variation = self.domain_name[:i] + alt_char + self.domain_name[i+1:]
                    variations.append(variation)
        
        return [f"{domain}.{self.tld}" for domain in set(variations)]
    
    def homophone_squatting(self):
        """Generate domains based on similar-sounding words."""
        homophone_map = {
            'hear': ['here'],
            'their': ['there', 'they\'re'],
            'to': ['too', 'two'],
            'sale': ['sail'],
            'right': ['write', 'rite']
        }
        
        variations = []
        for word, homophones in homophone_map.items():
            if word in self.domain_name.lower():
                for homophone in homophones:
                    variation = self.domain_name.lower().replace(word, homophone)
                    variations.append(variation)
        
        return [f"{domain}.{self.tld}" for domain in set(variations)]
    
    def tld_squatting(self):
        """Generate domains with alternative TLDs."""
        common_tlds = [
            'com', 'org', 'net', 'io', 'co', 'info', 
            'biz', 'us', 'me', 'online', 'shop'
        ]
        
        return [f"{self.domain_name}.{tld}" for tld in common_tlds if tld != self.tld]
    
    def combo_squatting(self):
        """Generate domains by adding keywords."""
        keywords = [
            'payment', 'login', 'secure', 'verify', 
            'account', 'billing', 'support', 'service'
        ]
        
        variations = [
            f"{self.domain_name}{keyword}.{self.tld}"
            for keyword in keywords
        ]
        
        return variations
    
    def save_domains_to_file(self, squatting_domains, validation_results=None, output_dir=None):
        """
        Save generated domains to a CSV file with optional validation details
        
        :param squatting_domains: List of generated squatting domains
        :param validation_results: Optional list of domain validation results
        :param output_dir: Optional directory to save the file
        """
        # Determine output directory
        if not output_dir:
            output_dir = os.getcwd()
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"domain_squatting_{timestamp}.csv"
        filepath = os.path.join(output_dir, filename)
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Prepare header row
                header = [
                    "Original Domain", 
                    "Squatting Domain", 
                    "Squatting Technique"
                ]
                
                # Add validation columns if results are provided
                if validation_results:
                    header.extend([
                        "Domain Status", 
                        "Registrar", 
                        "Creation Date", 
                        "Expiration Date"
                    ])
                
                # Write header
                writer.writerow(header)
                
                # Write domain details
                for idx, domain in enumerate(squatting_domains, 1):
                    row = [
                        self.domain_name,  # Original domain
                        domain,       # Squatting domain
                        self._determine_technique(domain)  # Technique
                    ]
                    
                    # Add validation details if available
                    if validation_results:
                        # Find matching validation result
                        validation_info = next(
                            (result for result in validation_results if result['domain'] == domain), 
                            None
                        )
                        
                        if validation_info:
                            status = "Available" if validation_info['can_be_registered'] else "Registered"
                            row.extend([
                                status,
                                validation_info['registrar'],
                                validation_info['creation_date'],
                                validation_info['expiration_date']
                            ])
                        else:
                            # Pad with N/A if no validation info
                            row.extend(["N/A", "N/A", "N/A", "N/A"])
                    
                    # Write row
                    writer.writerow(row)
            
            # Print success message
            print(f"\n Domains saved to: {filepath}")
            return filepath
        
        except Exception as e:
            print(f"Error saving domains: {e}")
            return None

    def _determine_technique(self, domain):
        """Determine the squatting technique used for a domain."""
        if domain.startswith(self.domain_name):
            return "Combo Squatting"
        elif domain.endswith(self.tld) and domain != f"{self.domain_name}.{self.tld}":
            return "TLD Squatting"
        elif any(char in domain for char in ['0', '@', '1', '!', '4', '3']):
            return "Character Replacement"
        elif any(char in domain for char in ['а', 'с', 'р', 'х']):
            return "Homograph Attack"
        else:
            return "Typosquatting"

    def generate_squatting_domains(self):
        """Combine all squatting techniques."""
        techniques = [
            self.typosquatting(),
            self.homograph_attack(),
            self.homophone_squatting(),
            self.tld_squatting(),
            self.combo_squatting()
        ]
        
        # Flatten and remove duplicates
        return list(set(domain for technique in techniques for domain in technique))

class DomainValidator:
    @staticmethod
    def is_connected():
        """
        Check internet connectivity with a very short timeout
        """
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except (socket.error, socket.timeout):
            return False

    @staticmethod
    def check_domain_availability(domain):
        """
        Check domain availability using multiple methods
        Returns a dictionary with detailed domain information
        """
        # Prepare result dictionary
        result = {
            'domain': domain,
            'is_registered': False,
            'registrar': 'N/A',
            'creation_date': 'N/A',
            'expiration_date': 'N/A',
            'can_be_registered': False,
            'validation_details': []
        }

        # Step 1: Basic Domain Format Check
        if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
            print(f" Checking WHOIS for {domain}: Invalid Domain")
            result['validation_details'].append("Invalid domain format")
            return result

        # Step 2: Internet Connectivity Check
        if not DomainValidator.is_connected():
            print(f" Checking WHOIS for {domain}: No Internet Connection")
            result['validation_details'].append("No internet connection")
            return result

        # Step 3: WHOIS Lookup
        try:
            import whois
            
            try:
                domain_info = whois.whois(domain)
                
                # Check if domain is registered
                if domain_info.domain_name:
                    result['is_registered'] = True
                    result['registrar'] = str(domain_info.registrar) if domain_info.registrar else 'Unknown'
                    result['creation_date'] = str(domain_info.creation_date) if domain_info.creation_date else 'N/A'
                    result['expiration_date'] = str(domain_info.expiration_date) if domain_info.expiration_date else 'N/A'
                    
                    print(f" Checking WHOIS for {domain}: Registered")
                    result['validation_details'].append("Domain registered via WHOIS")
                else:
                    print(f" Checking WHOIS for {domain}: AVAILABLE")
                    result['can_be_registered'] = True
                    result['validation_details'].append("Not found in WHOIS")
            
            except Exception as whois_error:
                # Simplify error message to a single, concise line
                error_message = str(whois_error).split('\n')[0]
                print(f" Checking WHOIS for {domain}: {error_message}")
                result['validation_details'].append(f"WHOIS error: {error_message}")
        
        except ImportError:
            # Fallback to basic domain check if whois library not installed
            print(f" Checking WHOIS for {domain}: WHOIS library not installed")

        # Step 4: Socket-based Availability Check
        try:
            socket.gethostbyname(domain)
            result['is_registered'] = True
        except socket.gaierror:
            result['can_be_registered'] = True
        except Exception as socket_error:
            print(f" Checking WHOIS for {domain}: Network Check Error")
            result['validation_details'].append(f"Network check error: {str(socket_error)}")

        return result

    @staticmethod
    def validate_domains(domains, max_workers=3):
        """
        Validate multiple domains with improved error handling and reduced timeout risk
        """
        print("\n Starting Domain Validation...")
        validated_domains = []
        
        # Further reduce workers to minimize network congestion
        max_workers = min(max_workers, len(domains))
        
        # Use ThreadPoolExecutor for concurrent domain checking
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Prepare domain validation
            domain_futures = {}
            for domain in domains:
                # Skip domains with invalid characters
                if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
                    continue
                
                # Submit domain check with a shorter individual timeout
                future = executor.submit(
                    DomainValidator.check_domain_availability, 
                    domain
                )
                domain_futures[future] = domain
            
            # Collect results with reduced timeout and error handling
            try:
                for future in concurrent.futures.as_completed(
                    domain_futures, 
                    timeout=20  # Reduced overall timeout
                ):
                    try:
                        result = future.result(timeout=5)  # Short timeout per domain
                        if result:
                            validated_domains.append(result)
                    except (concurrent.futures.TimeoutError, Exception):
                        # Silently ignore individual domain validation failures
                        continue
            except concurrent.futures.TimeoutError:
                # If overall timeout is reached, return partial results
                print("\n Validation process timed out. Returning partial results.")
        
        print(f"\n Validation Complete. {len(validated_domains)} domains processed.")
        return validated_domains

def main():
    print(r'''
                _____                        _          _____                   _   _   _                _____                           _             
                |  __ \                      (_)        / ____|                 | | | | (_)              / ____|                         | | 　 　 　 　
                | |  | | ___  _ __ ___   __ _ _ _ __   | (___   __ _ _   _  __ _| |_| |_ _ _ __   __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
                | |  | |/ _ \| '_ ` _ \ / _` | | '_ \   \___ \ / _` | | | |/ _` | __| __| | '_ \ / _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
                | |__| | (_) | | | | | | (_| | | | | |  ____) | (_| | |_| | (_| | |_| |_| | | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
                |_____/ \___/|_| |_| |_|\__,_|_|_| |_| |_____/ \__, |\__,_|\__,_|\__|\__|_|_| |_|\__, |  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                | |                             __/ |                                                 
                                                                |_|                            |___/                                                  

                ''')
    print("--------------------------------\nWelcome to the Domain Squatting Tool!\n--------------------------------\n")
    
    while True:
        domain = input("\nEnter a domain name (Ex: example.com): ").strip()
        
        if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
            print("Invalid domain format. Please try again.")
            continue
        
        squatter = DomainSquatter(domain)
        squatting_domains = squatter.generate_squatting_domains()
        
        print("\nGenerated Squatting Domains:")
        for idx, squatting_domain in enumerate(squatting_domains, 1):
            print(f"{idx}. {squatting_domain}")
        
        # New domain validation prompt
        validate_choice = input("\nWould you like to validate these domains? (y/n): ").lower()
        validation_results = None
        print("Here's a detailed explanation of the domain status messages:")
        print("Status: Registered - Means the domain is already owned by someone")
        print("Status: AVAILABLE - Means the domain is free and can be registered")
        print("Status: Invalid Domain - Means the domain does not meet basic formatting requirements due to incorrect characters, Missing top-level domain, OR Does not match the pattern name.tld ")
        if validate_choice == 'y':
            print("\nValidating domains... This may take a few moments.")
            validation_results = DomainValidator.validate_domains(squatting_domains)
            
            print("\nDomain Validation Results:")
            available_domains = []
            for domain_info in validation_results:
                status = "Available" if domain_info['can_be_registered'] else "Registered"
                
                print(f"Domain: {domain_info['domain']}")
                print(f"Status: {status}")
                print(f"Registrar: {domain_info['registrar']}")
                print(f"Creation Date: {domain_info['creation_date']}")
                print(f"Expiration Date: {domain_info['expiration_date']}")
                print("---")
                
                if domain_info['can_be_registered']:
                    available_domains.append(domain_info)
        
        # Save domains option
        save_choice = input("\nDo you want to save these domains to a file? (y/n): ").lower()
        if save_choice == 'y':
            output_dir = input("Enter output directory (press Enter for current directory): ").strip()
            squatter.save_domains_to_file(
                squatting_domains, 
                validation_results, 
                output_dir
            )
        
        choice = input("\nDo you want to generate domains for another domain? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
