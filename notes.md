# Regular Expressions (Regex) - A Quick Guide

### 1. **What is Regex?**
Regex is a sequence of characters that form a search pattern. It can be used to search, match, or replace strings in text. For example, finding a specific word or validating formats like emails or phone numbers.

---

### 2. **Basic Regex Syntax**

#### a. **Literal Characters**
These are the characters you want to match exactly in the text.

- `a` matches the letter `a`
- `b` matches the letter `b`

**Example**:  
Regex: `cat`  
Text: `"The cat is cute."`  
It will match the word "cat" in the text.

#### b. **Meta-characters**
Special characters that have specific meanings in regex.

- `.` (dot) matches **any single character** except newlines.
  - Example: `a.b` matches `acb`, `a1b`, `a_b`, etc.
- `^` matches the **beginning** of the string.
  - Example: `^abc` matches "abc" only at the beginning of a string.
- `$` matches the **end** of the string.
  - Example: `abc$` matches "abc" only at the end of the string.
  
---

### 3. **Character Classes**

Character classes define a set of characters to match.

- **`[ ]`**: Matches **any one** character inside the brackets.
  - Example: `[aeiou]` matches any vowel.
  - Example: `[0-9]` matches any digit.
  
- **`[^ ]`**: Matches any character **except** the ones inside the brackets.
  - Example: `[^a-z]` matches any character that’s not a lowercase letter.
  
---

### 4. **Quantifiers**

Quantifiers define **how many times** a pattern should match.

- **`*`**: Matches **0 or more** occurrences of the previous element.
  - Example: `a*` matches `""` (empty), `a`, `aa`, `aaa`, etc.
- **`+`**: Matches **1 or more** occurrences.
  - Example: `a+` matches `a`, `aa`, `aaa`, etc. (but not an empty string).
- **`?`**: Matches **0 or 1** occurrence.
  - Example: `a?` matches `""` (empty) or `a`.
- **`{n}`**: Matches **exactly n** occurrences of the preceding element.
  - Example: `a{3}` matches `aaa`.
- **`{n,}`**: Matches **n or more** occurrences.
  - Example: `a{2,}` matches `aa`, `aaa`, `aaaa`, etc.
- **`{n,m}`**: Matches between **n and m** occurrences.
  - Example: `a{2,4}` matches `aa`, `aaa`, or `aaaa`.

---

### 5. **Special Sequences**

- **`\d`**: Matches any **digit** (equivalent to `[0-9]`).
  - Example: `\d` matches `1`, `2`, `3`, etc.
  
- **`\w`**: Matches any **alphanumeric character** (letters and digits) plus the underscore (`_`).
  - Example: `\w` matches `a`, `A`, `3`, `_`, etc.
  
- **`\s`**: Matches any **whitespace character** (space, tab, newline).
  - Example: `\s` matches `" "`, `"\t"`, etc.
  
- **`\b`**: Matches a **word boundary** (the position between a word and a non-word character).
  - Example: `\bcat\b` matches the word "cat" but not "scatter".

---

### 6. **Grouping and Alternation**

- **`( )`**: **Groups** parts of the regex together to apply quantifiers or operations to them.
  - Example: `(abc)+` matches `abc`, `abcabc`, etc.

- **`|`**: Represents **alternation** (OR).
  - Example: `cat|dog` matches either `cat` or `dog`.

---

### 7. **Anchors**

- **`^`**: Anchors the match to the **start** of the string.
  - Example: `^cat` matches "cat" at the beginning of the string.
  
- **`$`**: Anchors the match to the **end** of the string.
  - Example: `cat$` matches "cat" at the end of the string.

---

### 8. **Escape Sequences**

Certain characters have special meanings in regex. To use them as literal characters, you need to escape them with a backslash `\`.

- **`\.`**: Matches a literal dot (`.`).
- **`\*`**: Matches a literal asterisk (`*`).
- **`\+`**: Matches a literal plus sign (`+`).
- **`\?`**: Matches a literal question mark (`?`).

Example:  
Regex: `a\+b`  
Text: `"a+b"`  
This matches "a+b" and not "ab".

---

### 9. **Example Regex Patterns**

1. **Matching a simple email**:
   - Regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
   - Explanation: Matches an email starting with one or more valid characters, followed by `@`, the domain, and then a dot and at least two letters for the TLD.

2. **Matching a phone number**:
   - Regex: `^\(\d{3}\) \d{3}-\d{4}$`
   - Explanation: Matches a phone number in the format `(123) 456-7890`.

3. **Matching a date (YYYY-MM-DD)**:
   - Regex: `^\d{4}-\d{2}-\d{2}$`
   - Explanation: Matches a date like "2024-12-05".

---

### 10. **Practical Tips**

- **Testing Regex**: Tools like [regex101](https://regex101.com/) let you test and understand your regex.
- **Greedy vs Lazy Matching**: By default, regex quantifiers are **greedy**, meaning they match as much text as possible. To make them **lazy** (match the smallest amount possible), use `?` after the quantifier. For example, `.*?` is lazy.
  
---

### 11. **Resources for Learning**

- **Regexr** (Interactive learning tool): [https://regexr.com/](https://regexr.com/)
- **Regular-Expressions.info** (Detailed guide): [https://www.regular-expressions.info/](https://www.regular-expressions.info/)
- **Regex101** (Testing and explanation): [https://regex101.com/](https://regex101.com/)

---

## Example: Matching Email Addresses with a Regular Expression
The string `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'` is a **regular expression (regex)** pattern used to match email addresses. Let's break it down:

1. **`r''`**: 
   - This is a raw string literal in Python. The `r` before the string tells Python not to escape special characters (like backslashes). This is helpful when writing regex patterns because backslashes are used frequently and could cause errors or confusion.

2. **`[a-zA-Z0-9._%+-]+`**:
   - `[a-zA-Z0-9._%+-]`: This defines a **character class**, which matches one of the characters inside the square brackets. Specifically, it matches any lowercase letter (`a-z`), uppercase letter (`A-Z`), digit (`0-9`), or any of the following special characters:
     - `.` (dot)
     - `_` (underscore)
     - `%`
     - `+`
     - `-`
   - The `+` after the character class means **one or more occurrences** of these characters. This part matches the local part of an email (the part before the `@`).

3. **`@`**:
   - This simply matches the **at symbol** (`@`) that separates the local part from the domain part of the email address.

4. **`[a-zA-Z0-9.-]+`**:
   - Similar to the previous part, this matches the **domain part** of the email address. It allows lowercase and uppercase letters, digits, dots (`.`), and hyphens (`-`).
   - The `+` means **one or more occurrences**, ensuring there is at least one character for the domain name.

5. **`\.`**:
   - The backslash (`\`) escapes the dot (`.`), which normally matches any character in regex. Here, it ensures that the dot is treated literally (i.e., it matches an actual period/dot, like in `gmail.com`).

6. **`[a-zA-Z]{2,}`**:
   - `[a-zA-Z]`: Matches any letter, either lowercase or uppercase.
   - `{2,}`: This specifies that the preceding character class must appear **at least twice**. This part ensures that the email domain has a valid top-level domain (TLD) like `.com`, `.org`, `.net`, etc.

### Summary:
This regex pattern matches email addresses in the following format:

- One or more alphanumeric characters or special characters (`._%+-`) before the `@`.
- The `@` symbol separates the local part and domain.
- The domain part consists of alphanumeric characters, dots, and hyphens.
- A dot (`.`) is followed by two or more alphabetic characters representing the top-level domain (like `.com`, `.org`, etc.).

### Example matches:
- `user@example.com`
- `test_user+123@subdomain.example.co.uk`
- `name.lastname@domain.io`

This pattern does not match every possible email format defined by the full email specification (RFC 5322), but it works for common email formats used in practice.

---

A **data sanitization strategy** refers to the processes and techniques used to cleanse and protect data, ensuring that it is free from errors, inconsistencies, or unauthorized access. The goal is to ensure that data is accurate, valid, and secure while also meeting privacy, compliance, and security standards. Data sanitization can be performed across various stages of the data lifecycle, from collection to deletion.

# Data sanitization strategy

### 1. **Data Classification**
   - **Identify sensitive data**: Categorize data into different types (e.g., sensitive, personal, public) to understand the level of protection required. For example, personally identifiable information (PII), financial data, and medical records require strict sanitization.
   - **Tagging and labeling**: Mark sensitive data for protection and ensure it is managed according to regulatory requirements (e.g., GDPR, HIPAA).

### 2. **Data Collection & Validation**
   - **Input Validation**: Ensure that data entered into systems is sanitized to prevent invalid, malicious, or erroneous data from being collected.
     - Use techniques like **input validation** to prevent SQL injection, cross-site scripting (XSS), and other forms of malicious data injection.
     - Enforce **data type checks**, **range checks**, and **format checks** to ensure data integrity.
   - **Data Formatting**: Enforce standard formats (e.g., dates, phone numbers, addresses) during collection to avoid inconsistencies and errors.

### 3. **Data Cleaning**
   - **Remove duplicates**: Identify and remove duplicate records to avoid redundancy and potential data corruption.
   - **Standardize data**: Normalize data to ensure consistency across systems (e.g., converting all text to uppercase/lowercase, standardizing units of measure).
   - **Correct errors**: Use automated tools or manual procedures to identify and correct data inaccuracies.

### 4. **Data Masking**
   - **Data Masking**: For sensitive information, apply techniques like data masking or tokenization to replace sensitive data with obfuscated or random values.
   - This is especially important in development or testing environments where real data is not necessary.
     - For example, replace actual social security numbers or credit card details with masked values like "XXX-XX-1234."

### 5. **Data Anonymization**
   - **Anonymize or Pseudonymize Data**: Remove personally identifiable information (PII) from datasets or replace it with pseudonyms to preserve privacy. This is especially critical in analytics or data-sharing scenarios where personal identification should be avoided.
     - Example: Anonymizing names, addresses, or phone numbers while retaining general trends.

### 6. **Data Encryption**
   - **Encrypt sensitive data** both at rest and in transit to protect against unauthorized access. Use industry-standard encryption algorithms (e.g., AES-256) and key management techniques.
   - Ensure that encryption keys are stored securely and rotated periodically.

### 7. **Data Access Control**
   - **Role-based Access Control (RBAC)**: Define clear policies on who can access, modify, or delete data based on their roles within the organization.
   - Implement **least privilege** principles to ensure that only authorized individuals have access to sensitive or critical data.
   - Monitor and log all access to sensitive data for auditing and security purposes.

### 8. **Data Deletion and Destruction**
   - **Secure Deletion**: When data is no longer needed, ensure it is securely deleted to prevent unauthorized recovery.
     - Use tools that comply with data destruction standards (e.g., DoD 5220.22-M, NIST SP 800-88).
     - Overwrite data multiple times, or use physical destruction methods like shredding drives for highly sensitive data.
   - Ensure that deletion practices are documented, auditable, and compliant with regulations.

### 9. **Data Auditing and Monitoring**
   - **Continuous Monitoring**: Implement real-time monitoring systems to detect unusual data access, modification, or anomalies.
   - **Auditing and Logging**: Maintain an audit trail of all data sanitization activities, including access, modification, and deletion actions, to comply with regulatory and internal policies.

### 10. **Compliance & Regulatory Considerations**
   - **Follow Regulations**: Adhere to relevant data protection regulations, such as the **General Data Protection Regulation (GDPR)**, **Health Insurance Portability and Accountability Act (HIPAA)**, or **California Consumer Privacy Act (CCPA)**.
   - Regularly review compliance standards and ensure that the sanitization methods meet or exceed legal requirements for data protection.

### 11. **Regular Data Sanitization Reviews**
   - **Ongoing Review**: Regularly review and update the data sanitization strategy to adapt to evolving security threats, new compliance requirements, and data growth.
   - Train staff and stakeholders on data privacy best practices and the importance of data sanitization.

### 12. **Automation of Data Sanitization**
   - Leverage automated tools and AI to detect and clean sensitive or incorrect data at scale, especially in large datasets.
   - Automate the regular sanitization tasks, like removing duplicates or standardizing formats, to improve efficiency and consistency.

By following a comprehensive data sanitization strategy, organizations can mitigate risks related to data breaches, maintain the integrity of their data, and ensure compliance with applicable laws and regulations.

---
# Performing preprocessing on the data
- 1. Importing the necessary libraries
- 2. Loading the data
- 3. Checking for missing values
- 4. Checking for duplicates
- 5. Checking for the data types
- 6. Checking for the unique values in the columns
- 7. Checking for the distribution of the target variable
- 8. Checking for the correlation between the features
- 9. Checking for the outliers
- 10. Performing the feature engineering
- 11. Splitting the data into train and test
- 12. Performing the feature scaling
- 13. Performing the feature selection
- 14. Performing the model building
- 15. Performing the model evaluation
- 16. Performing the model tuning
- 17. Performing the model deployment