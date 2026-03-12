# Step-by-Step Guide: Setting Up YubiKey Hardware Security Keys

**Source:** Shannon Morse (YouTube)
**Video ID:** MnCqlOtOEWo
**Upload Date:** 2026-02-07

---

## What This Guide Covers

How to buy, set up, and use YubiKey hardware security keys for phishing-resistant two-factor authentication across all your online accounts.

---

## Prerequisites

- A computer with USB-C port (or USB-A with adapter)
- A smartphone with NFC capability (for tap-to-authenticate)
- Online accounts to protect (email, password manager, banking, etc.)

---

## Step 1: Purchase Two YubiKeys

1. Buy **two YubiKey 5 Series (USB-C + NFC)** — one primary, one backup
2. Available at Best Buy, Amazon, or direct from Yubico
3. Two-key bundles exist and are more cost-effective

---

## Step 2: Understand the Protocols

| Protocol | When It's Used |
|----------|---------------|
| **FIDO2 / WebAuthn** | Modern websites (Google, Microsoft, GitHub, etc.) — use this whenever available |
| **U2F** | Older services that haven't upgraded to FIDO2 |
| **OTP** | Legacy systems that only support one-time codes |
| **Smart Card / PIV** | Workplace logins, SSH, PGP signing (developer use) |

**Why it's phishing-resistant:** The key's credential is cryptographically bound to the exact domain. A fake site on a different domain cannot extract or replay the credential.

---

## Step 3: Secure Your Email First

1. Log into your email provider (Gmail, Proton Mail, Yahoo, etc.)
2. Navigate to **Settings > Security > Two-Factor Authentication**
3. Look for "Security Key" or "Passkey" option
4. Click "Add a security key"
5. Insert your YubiKey into USB-C port (or tap via NFC on phone)
6. Follow the on-screen prompts
7. **Set a PIN if offered** — protects against physical theft
8. **Repeat with your backup key**
9. **Save any recovery codes** — print and store offline in a secure location

---

## Step 4: Secure Your Password Manager

- This is your second-highest priority (after email)
- Same process: Settings > Security > Add security key
- Register both primary and backup keys
- Save recovery codes offline

---

## Step 5: Add to All Other Accounts

Work through your accounts in priority order:
1. Banking / financial services
2. Cloud storage (Google Drive, Dropbox, iCloud)
3. Social media
4. Developer accounts (GitHub, AWS, etc.)
5. Everything else that supports security keys

---

## Step 6: Choose Between Passkeys and Security Keys Per Service

| Type | Pros | Cons |
|------|------|------|
| **Synced passkeys** | Convenient, travel across devices | Credential copies exist in cloud |
| **Hardware-bound passkeys** | Highest assurance, never leaves device | Must physically have the key |

- Use hardware-bound for critical accounts (email, banking, password manager)
- Synced passkeys are acceptable for lower-risk accounts

---

## Step 7: Personal Threat Model Assessment

Consider your specific risks:
- Natural disasters (fire, flood) — store backup key offsite or in fireproof safe
- Theft risk (commuting, travel) — keep backup key in a separate location
- Data sensitivity — if you handle proprietary/sensitive data, hardware-bound only
- Household risks (pets, children) — store keys securely

---

## Best Practices Checklist

- [ ] Register backup key on every account
- [ ] Use a PIN when offered
- [ ] Lock devices when key is plugged in
- [ ] Email and password manager secured first
- [ ] Prefer FIDO2/WebAuthn over OTP
- [ ] Recovery codes printed and stored offline
- [ ] Backup key stored in separate physical location

---

## Key Takeaway

> Hardware security keys provide phishing-resistant authentication that SMS codes and authenticator apps cannot match. Buy two YubiKey 5 Series (USB-C + NFC), secure your email and password manager first, and save recovery codes offline. The setup per service takes minutes; the protection is permanent.

*Guide derived from: YubiKey 101 – What It Is, How It Works, and How to Set It Up 🔐.txt*
