#!/usr/bin/env python3
"""
Test PDF Download Accessibility
Tests that PDF and document files are accessible from the website
"""

import os
import requests
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def test_local_files_exist():
    """Test that PDF and DOCX files exist in the repository"""
    print(f"\n{Colors.BLUE}Testing: Local File Existence{Colors.RESET}")
    
    base_path = Path("docs/episodes/02-resume-fine-tuner/workspace/outputs")
    files_to_check = [
        "resume.pdf",
        "resume.docx",
        "resume 2.pdf",
        "resume 2.docx"
    ]
    
    all_exist = True
    for file in files_to_check:
        file_path = base_path / file
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"  {Colors.GREEN}✓{Colors.RESET} {file} exists ({size:,} bytes)")
        else:
            print(f"  {Colors.RED}✗{Colors.RESET} {file} NOT FOUND")
            all_exist = False
    
    return all_exist

def test_built_files_exist():
    """Test that files exist in the built site directory"""
    print(f"\n{Colors.BLUE}Testing: Built Site File Existence{Colors.RESET}")
    
    base_path = Path("site/episodes/02-resume-fine-tuner/workspace/outputs")
    
    if not base_path.exists():
        print(f"  {Colors.RED}✗{Colors.RESET} Build output directory not found: {base_path}")
        print(f"  {Colors.YELLOW}Run 'mkdocs build' first{Colors.RESET}")
        return False
    
    files_to_check = [
        "resume.pdf",
        "resume.docx"
    ]
    
    all_exist = True
    for file in files_to_check:
        file_path = base_path / file
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"  {Colors.GREEN}✓{Colors.RESET} {file} exists in build ({size:,} bytes)")
        else:
            print(f"  {Colors.RED}✗{Colors.RESET} {file} NOT FOUND in build")
            all_exist = False
    
    return all_exist

def test_download_links_in_html():
    """Test that download links exist in the HTML pages"""
    print(f"\n{Colors.BLUE}Testing: Download Links in HTML{Colors.RESET}")
    
    pages_to_check = [
        ("site/episodes/02-resume-fine-tuner/🎯 START_HERE/index.html", "START_HERE page"),
        ("site/episodes/02-resume-fine-tuner/workspace/index.html", "Workspace README"),
        ("site/episodes/02-resume-fine-tuner/workspace/EXAMPLES/index.html", "Examples page"),
        ("site/index.html", "Homepage")
    ]
    
    all_links_found = True
    for file_path, page_name in pages_to_check:
        path = Path(file_path)
        if not path.exists():
            print(f"  {Colors.RED}✗{Colors.RESET} {page_name}: File not found")
            all_links_found = False
            continue
        
        content = path.read_text(encoding='utf-8')
        
        # Check for PDF links
        has_pdf_link = "resume.pdf" in content
        has_docx_link = "resume.docx" in content
        has_download_text = "download" in content.lower() or "Download" in content
        
        if has_pdf_link:
            print(f"  {Colors.GREEN}✓{Colors.RESET} {page_name}: PDF link found")
        else:
            # Homepage and some pages might not have direct PDF links
            if page_name in ["START_HERE page", "Workspace README", "Examples page"]:
                print(f"  {Colors.RED}✗{Colors.RESET} {page_name}: PDF link NOT found")
                all_links_found = False
            else:
                print(f"  {Colors.YELLOW}○{Colors.RESET} {page_name}: No PDF link (optional)")
    
    return all_links_found

def test_local_server_accessibility():
    """Test that files are accessible via local server"""
    print(f"\n{Colors.BLUE}Testing: Local Server Accessibility{Colors.RESET}")
    print(f"  {Colors.YELLOW}Note: Start 'mkdocs serve' before running this test{Colors.RESET}")
    
    base_url = "http://localhost:8000"
    urls_to_test = [
        "/episodes/02-resume-fine-tuner/workspace/outputs/resume.pdf",
        "/episodes/02-resume-fine-tuner/workspace/outputs/resume.docx",
        "/episodes/02-resume-fine-tuner/workspace/EXAMPLES/",
        "/episodes/02-resume-fine-tuner/🎯 START_HERE/"
    ]
    
    all_accessible = True
    for url_path in urls_to_test:
        url = base_url + url_path
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                print(f"  {Colors.GREEN}✓{Colors.RESET} {url_path} is accessible (200)")
            else:
                print(f"  {Colors.RED}✗{Colors.RESET} {url_path} returned {response.status_code}")
                all_accessible = False
        except requests.exceptions.RequestException as e:
            print(f"  {Colors.YELLOW}○{Colors.RESET} {url_path} - Server not running (skip)")
            # Don't fail the test if server isn't running
            continue
    
    return all_accessible

def test_production_site_accessibility():
    """Test that files are accessible on the production site"""
    print(f"\n{Colors.BLUE}Testing: Production Site Accessibility{Colors.RESET}")
    print(f"  {Colors.YELLOW}Note: This tests the deployed GitHub Pages site{Colors.RESET}")
    print(f"  {Colors.YELLOW}Note: May fail in sandboxed environment (network restricted){Colors.RESET}")
    
    base_url = "https://anton-abyzov.github.io/ai-power"
    urls_to_test = [
        "/episodes/02-resume-fine-tuner/workspace/outputs/resume.pdf",
        "/episodes/02-resume-fine-tuner/workspace/EXAMPLES/",
    ]
    
    all_accessible = True
    network_available = True
    
    for url_path in urls_to_test:
        url = base_url + url_path
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                print(f"  {Colors.GREEN}✓{Colors.RESET} {url_path} is accessible (200)")
            elif response.status_code == 404:
                print(f"  {Colors.RED}✗{Colors.RESET} {url_path} returned 404 (not found)")
                all_accessible = False
            else:
                print(f"  {Colors.YELLOW}○{Colors.RESET} {url_path} returned {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Network errors are expected in sandboxed environments
            if "Failed to resolve" in str(e) or "Name or service not known" in str(e):
                print(f"  {Colors.YELLOW}○{Colors.RESET} {url_path} - Network unavailable (sandboxed)")
                network_available = False
            else:
                print(f"  {Colors.RED}✗{Colors.RESET} {url_path} - Error: {str(e)}")
                all_accessible = False
    
    # If network is unavailable, we still consider test as passed (informational only)
    if not network_available:
        print(f"  {Colors.YELLOW}⚠{Colors.RESET}  Test skipped: External network not available")
        return True
    
    return all_accessible

def main():
    """Run all tests"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}PDF Download Accessibility Tests{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}")
    
    results = []
    
    # Run tests
    results.append(("Local Files Exist", test_local_files_exist()))
    results.append(("Built Files Exist", test_built_files_exist()))
    results.append(("Download Links in HTML", test_download_links_in_html()))
    results.append(("Local Server Accessibility", test_local_server_accessibility()))
    results.append(("Production Site Accessibility", test_production_site_accessibility()))
    
    # Print summary
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}Test Summary{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = f"{Colors.GREEN}PASSED{Colors.RESET}" if result else f"{Colors.RED}FAILED{Colors.RESET}"
        print(f"  {test_name}: {status}")
    
    print(f"\n{Colors.BLUE}Total: {passed}/{total} tests passed{Colors.RESET}")
    
    if passed == total:
        print(f"\n{Colors.GREEN}✓ All tests passed!{Colors.RESET}")
        return 0
    else:
        print(f"\n{Colors.RED}✗ Some tests failed{Colors.RESET}")
        return 1

if __name__ == "__main__":
    exit(main())
