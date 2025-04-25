# 🔢 Prime Palindrome Finder (Miller-Rabin Based)

This Python project efficiently finds all **prime palindromic numbers** between any two very large integers — even up to **1 trillion+** — using a combination of:
- Custom palindrome generation logic
- The probabilistic **Miller-Rabin primality test**

Perfect for high-performance number theory tasks, coding challenges, or research-oriented exploration of numeric patterns.

---

## 🧠 What Are Prime Palindromes?

A number is a **prime palindrome** if:
- It reads the same forward and backward (e.g. `131`, `727`)
- It is a **prime number** (only divisible by `1` and itself)

---

## 🚀 Features

- 🔍 Efficient palindrome generation based on digit mirroring
- ⚡ Fast primality checking with the **Miller-Rabin algorithm**
- 📈 Handles extremely large ranges (tested up to `1e34`)
- 🕒 Tracks and displays execution time
- 📊 Prints a summary with first and last 3 results (if results > 6)

---

## 📂 Project Structure

```bash
Prime_palindrome/
│
├── rabin miller.py     # Main script that runs the palindrome + primality logic
├── .idea/              # (Optional) PyCharm config files
└── README.md           # You're here!

