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

## Corelation and covariance
- **Covariance** is a measure of how changes in one variable are associated with changes in a second variable.
- **Correlation** is a standardized measure of covariance that ranges from -1 to 1. It provides insights into the direction and strength of the relationship between two variables.

---