# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand data representation and number systems used by computers:
- Perform manual, step-by-step conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16) number systems.
- Verify manual conversion results using Python's built-in functions.
- Build and test an interactive Python utility (`number_converter.py`) that converts decimal integers to binary and hexadecimal.
- Investigate character encoding schemes (ASCII and UTF-8), including the bitwise representation of letters and non-ASCII characters.

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
- **Method:** Repeated division by 2, recording remainders:
  - $13 \div 2 = 6$, remainder $1$ (Least Significant Bit - LSB)
  - $6 \div 2 = 3$, remainder $0$
  - $3 \div 2 = 1$, remainder $1$
  - $1 \div 2 = 0$, remainder $1$ (Most Significant Bit - MSB)
- Reading remainders from bottom to top (MSB to LSB): **$1101_2$**
- **Verification using positional weights:** $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$.

#### 2. Convert decimal 25 to binary
- **Method:** Repeated division by 2:
  - $25 \div 2 = 12$, remainder $1$ (LSB)
  - $12 \div 2 = 6$, remainder $0$
  - $6 \div 2 = 3$, remainder $0$
  - $3 \div 2 = 1$, remainder $1$
  - $1 \div 2 = 0$, remainder $1$ (MSB)
- Reading remainders from bottom to top: **$11001_2$**
- **Verification using positional weights:** $(1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 16 + 8 + 0 + 0 + 1 = 25_{10}$.

#### 3. Convert binary 1010 to decimal
- **Method:** Summing positional powers of 2 ($2^3, 2^2, 2^1, 2^0$):
  - $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$
  - $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$
  - $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$

#### 4. Convert binary 1101 to decimal
- **Method:** Summing positional powers of 2 ($2^3, 2^2, 2^1, 2^0$):
  - $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
  - $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$
  - $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$

#### 5. Convert hexadecimal A to decimal
- **Method:** In hexadecimal (base 16), digits 0–9 correspond to 0–9, and letters A–F represent values 10–15 ($A=10, B=11, C=12, D=13, E=14, F=15$).
  - Digit $A$ has value $10$.
  - Position weight: $10 \times 16^0 = 10 \times 1 = \mathbf{10_{10}}$

#### 6. Convert hexadecimal 1F to decimal
- **Method:** Summing positional powers of 16 ($16^1, 16^0$):
  - In $1F$, digit $1$ is at position 1 ($16^1$) and digit $F$ ($=15$) is at position 0 ($16^0$):
  - $(1 \times 16^1) + (15 \times 16^0)$
  - $= 16 + 15 = \mathbf{31_{10}}$

#### 7. Convert binary 1111 to hexadecimal
- **Method:** Each hexadecimal digit corresponds directly to a 4-bit binary group (nibble):
  - Bit evaluation: $(1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) = 8 + 4 + 2 + 1 = 15_{10}$.
  - The decimal value $15$ in hexadecimal notation is represented by the single symbol **$F_{16}$** (or `0xF`).

---

### Task 5.2 — Verify using Python
Each calculation was verified interactively using Python's built-in functions:

| Problem from Task 5.1 | Python expression tested | Returned output | Matches manual calculation? |
|---|---|---|---|
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes, matches $1101_2$ (`0b` indicates binary prefix). |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes, matches $11001_2$. |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | Yes, matches $10_{10}$. |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | Yes, matches $13_{10}$. |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | Yes, matches $10_{10}$. |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | Yes, matches $31_{10}$. |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes, matches $F_{16}$ (`0x` indicates hex prefix). |

---

### Task 5.3 — Python number converter
Created `mission-05-numbers-data/number_converter.py` to allow interactive conversions of decimal numbers into binary and hexadecimal.

#### Built-in Python functions explained:
- `input()`: Pauses program execution, displays a user prompt, and reads user keystrokes from standard input as a string.
- `int(value)`: Parses the input string and converts it into a Python integer data type for arithmetic.
- `bin(number)`: Converts an integer to its binary string representation prefixed with `'0b'`.
- `hex(number)`: Converts an integer to its hexadecimal string representation prefixed with `'0x'`.

#### Test Results:
The program was executed from Terminal with multiple test inputs:

| Test number | Binary output | Hexadecimal output | Notes |
|---|---|---|---|
| **42** | `0b101010` (`101010`) | `0X2A` (`2A`) | $(32 + 8 + 2 = 42)$; $(2 \times 16 + 10 = 42)$. Verified. |
| **156** | `0b10011100` (`10011100`) | `0X9C` (`9C`) | $(128 + 16 + 8 + 4 = 156)$; $(9 \times 16 + 12 = 156)$. Verified. |
| **255** | `0b11111111` (`11111111`) | `0XFF` (`FF`) | 8 bits all set to 1 (one full byte); two hex $F$ digits. Verified. |
| **13** | `0b1101` (`1101`) | `0XD` (`D`) | Directly matches Task 5.1 problem 1. Verified. |

---

### Task 5.4 — How is text stored?

#### 1. ASCII Codes for 'A' and 'a':
- Uppercase **'A'**: Decimal code **65** (Binary: `01000001`, Hex: `0x41`).
- Lowercase **'a'**: Decimal code **97** (Binary: `01100001`, Hex: `0x61`).
- **Bit observation:** The numerical difference is $97 - 65 = 32$. In binary, bit 5 ($2^5 = 32$) is `0` for uppercase `'A'` and toggled to `1` for lowercase `'a'`.

#### 2. Why computers need an encoding standard:
Computers operate strictly with binary electronic states (0s and 1s) and cannot natively store human letters or language symbols. An encoding standard provides a universally agreed translation table mapping specific numbers to specific characters, ensuring that a text document created on one computer is rendered with identical characters when opened on another computer.

#### 3. Character outside basic ASCII:
Basic ASCII uses 7 bits and only defines 128 characters (0–127), which covers the English alphabet, numerals, and common punctuation. A character outside basic ASCII is the Indian Rupee symbol **₹** (Unicode code point `U+20B9`) or the Euro currency symbol **€** (`U+20AC`), both of which require modern multi-byte encodings like UTF-8 (using 3 bytes) to be represented in digital files.

---

## 3. Commands / tools used
- `python3`: Used interactively and in scripts to verify conversions.
- `bin()`, `hex()`, `int()`, `input()`, `ord()`: Built-in Python conversion and character encoding functions.
- `cat`: Verified script contents.
- macOS Terminal: Executed interactive converter tests.

---

## 4. My understanding
- Base 10 (decimal) is intuitive for humans, but computers physically use Base 2 (binary) because transistors are either off (0) or on (1).
- Base 16 (hexadecimal) is a compact, human-readable shorthand for binary: every 4 binary bits (a nibble) maps directly to exactly one hexadecimal digit ($0\text{--}9, A\text{--}F$).
- Character encoding systems (ASCII and UTF-8) extend binary representation to human languages, bridging electronic hardware and global communication.

---

## 5. Difficulties faced
- Remembering whether to read remainders top-to-bottom or bottom-to-top during repeated division (bottom-to-top is correct because the last division produces the most significant bit).
- Understanding Python's string prefixes (`0b` and `0x`) and stripping them for clean output formatting.

---

## 6. How I resolved them
- Double-checked all manual conversions by calculating positional powers from right to left to verify the sum.
- Used Python slice notation (`[2:]`) to cleanly separate raw prefix indicators from the numerical digits.

---

## 7. Evidence / files
- Conversion script: `mission-05-numbers-data/number_converter.py`
- Mission documentation: `mission-05-numbers-data/README.md`
- Verification logs: Python interactive outputs and four terminal test runs.

---

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
