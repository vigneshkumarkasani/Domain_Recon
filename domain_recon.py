import whois
import dns.resolver
import requests
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor
import os

# Global flag to control cancellation
cancel_flag = threading.Event()
subdomain_wordlist = "subdomains.txt"
directory_wordlist = "directories.txt"

# Function to log results
def log_result(domain, data):
    log_file = f"{domain}_recon.log"
    with open(log_file, "a") as log:
        log.write(data + "\n")

# WHOIS Lookup
def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        result = f"\n[+] WHOIS Information:\nDomain: {info.domain_name}\nRegistrar: {info.registrar}\n" \
                 f"Creation: {info.creation_date}\nExpiration: {info.expiration_date}\nNS: {info.name_servers}\n"
        log_result(domain, result)
        return result
    except Exception as e:
        return f"[-] WHOIS lookup failed: {e}\n"

# DNS Enumeration
def dns_enumeration(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]
    result = "\n[+] DNS Records:\n"
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            result += f"{record}: {[str(rdata) for rdata in answers]}\n"
        except Exception:
            pass
    log_result(domain, result)
    return result

# GUI Setup
root = tk.Tk()
root.title("Domain Recon Tool")
root.configure(bg="#1e1e1e")
root.geometry("900x550")
root.resizable(True, True)

# Styling
font_style = ("Courier", 12)
label_style = {"fg": "#00ff00", "bg": "#1e1e1e", "font": font_style}
entry_style = {"bg": "#333", "fg": "#00ff00", "insertbackground": "#00ff00", "font": font_style, "width": 50}
button_style = {"bg": "#222", "fg": "#00ff00", "font": font_style, "activebackground": "#00aa00", "borderwidth": 2}

# Widgets
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10, padx=10, fill="x")

tk.Label(frame, text="Enter Domain:", **label_style).pack(side="left", padx=10)
domain_entry = tk.Entry(frame, **entry_style)
domain_entry.pack(side="left", padx=10, expand=True, fill="x")

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10, fill="x")

run_button = tk.Button(button_frame, text="Start Scan", command=lambda: threading.Thread(target=run_recon).start(), **button_style)
run_button.pack(side="left", padx=10, expand=True, fill="x")

copy_button = tk.Button(button_frame, text="Copy Results", command=lambda: copy_results(), **button_style)
copy_button.pack(side="left", padx=10, expand=True, fill="x")

clear_button = tk.Button(button_frame, text="Clear Output", command=lambda: result_text.delete(1.0, tk.END), **button_style)
clear_button.pack(side="left", padx=10, expand=True, fill="x")

result_text = scrolledtext.ScrolledText(root, width=100, height=20, bg="#111", fg="#00ff00", font=font_style, insertbackground="#00ff00")
result_text.pack(padx=10, pady=10, expand=True, fill="both")

status_label = tk.Label(root, text="Status: Ready", fg="#ffffff", bg="#1e1e1e", font=("Courier", 10))
status_label.pack(pady=5, fill="x")

# Run Recon
def run_recon():
    domain = domain_entry.get().strip()
    if not domain:
        messagebox.showerror("Error", "Please enter a domain.")
        return
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"[+] Scanning {domain}...\n")
    status_label.config(text=f"Status: Scanning {domain}...")
    root.update_idletasks()
    
    result_text.insert(tk.END, whois_lookup(domain))
    result_text.insert(tk.END, dns_enumeration(domain))
    result_text.insert(tk.END, "\n[+] Scan Complete!\n")
    status_label.config(text="Status: Scan Complete")

# Copy Results
def copy_results():
    root.clipboard_clear()
    root.clipboard_append(result_text.get(1.0, tk.END))
    root.update()
    messagebox.showinfo("Copied", "Results copied to clipboard.")

root.mainloop()
