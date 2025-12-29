# CLAUDE.md - Kriptografi Asimetrik E-Book Project

## Project Overview

This is an interactive e-book for **RK222 Kriptografi Asimetrik** (Asymmetric Cryptography) course at Politeknik Siber dan Sandi Negara. Built with Quarto, it supports the flipped classroom model defined in RPS v3.0.

## Technology Stack

- **Publishing**: Quarto (book project type)
- **Language**: Bahasa Indonesia (primary), English (code/technical terms)
- **Code**: Python 3.10+ with cryptography, pycryptodome, sympy libraries
- **Output Formats**: HTML (primary), PDF, EPUB

## Project Structure

```
kriptografi-asimetrik-ebook/
├── _quarto.yml          # Main configuration
├── index.qmd            # Landing page
├── preface.qmd          # Kata pengantar
├── chapters/            # 14 chapters (01-14)
├── labs/                # 12 labs
├── assessments/         # Pre-quizzes, problem sets, quizzes
├── appendices/          # Reference materials
├── images/              # Figures and diagrams
├── code/                # Standalone Python files
├── styles/              # Custom CSS/SCSS
└── latex/               # PDF customization
```

## Content Guidelines

### Chapter Structure
Every chapter MUST follow this template:
1. Learning Objectives (aligned with CPMK)
2. Pre-Reading Checklist (video, pre-quiz)
3. Introduction with real-world motivation
4. Core content sections with code examples
5. Security Considerations (where applicable)
6. Summary with key takeaways
7. Self-Check Questions (with expandable answers)
8. Practice Problems
9. References

### Lab Structure
Every lab MUST include:
1. Overview table (duration, difficulty, prerequisites, CPMK)
2. Learning Objectives
3. Background/theory review
4. Pre-lab preparation
5. Step-by-step parts with checkpoints
6. Optional challenge section
7. Submission requirements
8. Troubleshooting section

### Code Standards
- All Python code must be PEP 8 compliant
- Use type hints where appropriate
- Include docstrings for all functions
- All code must execute without errors
- Use `cryptography` library for production code
- Custom implementations for educational purposes only

### Diagram Standards

**IMPORTANT**: All diagrams must follow official standards. See [DIAGRAM_STANDARDS.md](DIAGRAM_STANDARDS.md) for complete guide.

#### Quick Reference

**Color Palette** (Poltek SSN Official):
```python
COLORS = {
    'primary':    '#1a5f7a',  # Dark teal - Main elements
    'secondary':  '#57837b',  # Medium teal - Supporting
    'accent':     '#c4dfdf',  # Light teal - Backgrounds
    'highlight':  '#f26b60',  # Coral - Important points
    'success':    '#28a745',  # Green - Valid/correct
    'warning':    '#ffc107',  # Yellow - Caution
    'danger':     '#dc3545',  # Red - Errors/attacks
}
```

**Tool Selection**:
| Need to show... | Use this tool |
|----------------|---------------|
| Algorithm steps | Mermaid flowchart |
| Protocol exchange | Mermaid sequence |
| Performance data | Python matplotlib |
| EC visualization | Python matplotlib |
| System architecture | Mermaid graph |

**Templates Available**:
- `images/templates/mermaid-flowchart-template.mmd`
- `images/templates/mermaid-sequence-template.mmd`
- `images/templates/matplotlib-plot-template.py`
- `images/templates/matplotlib-bar-chart-template.py`
- `images/templates/ec-plot-template.py`

**Naming Convention**:
```
Format: chXX-figYY-description.ext

Examples:
✓ ch04-fig01-rsa-keygen.mmd
✓ ch07-fig03-ec-addition.py
✗ diagram1.png
✗ rsa_flow.jpg
```

**Usage in Quarto**:
````markdown
```{mermaid}
%%| label: fig-unique-id
%%| fig-cap: "Descriptive caption"
%%| fig-alt: "Accessibility description"
%%| code-fold: true
%%| code-summary: "Show diagram source"

flowchart TD
    A[Start] --> B[End]

    style A fill:#1a5f7a,color:#fff
    style B fill:#1a5f7a,color:#fff
```
````

**IMPORTANT**: Always use `code-fold: true` for mermaid diagrams to hide source code by default. Students see the diagram first, can expand to view source if needed.

**Diagram Checklist**:
- [ ] Uses official color palette
- [ ] Follows naming convention
- [ ] Has fig-cap (caption)
- [ ] Has fig-alt (accessibility)
- [ ] Source file saved (.mmd, .py)
- [ ] PNG at 300 DPI
- [ ] Tested in HTML and PDF
- [ ] Consistent with other diagrams

**Resources**:
- Complete guide: [DIAGRAM_STANDARDS.md](DIAGRAM_STANDARDS.md)
- Quick lookup: [DIAGRAM_QUICK_REFERENCE.md](DIAGRAM_QUICK_REFERENCE.md)
- Summary: [DIAGRAM_STANDARDS_SUMMARY.md](DIAGRAM_STANDARDS_SUMMARY.md)

### Quarto Features to Use

#### Callouts
```qmd
::: {.callout-note}
## Key Insight
Content here
:::

::: {.callout-warning}
## Security Warning
Content here
:::

::: {.callout-tip}
## Pro Tip
Content here
:::

# Expandable content
::: {.callout-note collapse="true"}
## Solution (Click to expand)
Answer here
:::
```

#### Tabsets
```qmd
::: {.panel-tabset}
## Python
```python
code here
```
## OpenSSL
```bash
command here
```
:::
```

#### Code Annotations
```qmd
```python
def example():
    x = 1  # <1>
    y = 2  # <2>
```
1. First annotation
2. Second annotation


#### Definition Lists

**IMPORTANT**: Always add blank line AFTER `:` for proper rendering.

**Correct**  ✓:

```markdown
**Term Name**: 

- list item 1
- list item 2
```

**Incorrect** ✗:
```markdown
**Term Name**: 
- list item 1
- list item 2
```

**Why**: Without blank line, some Markdown processors may not render definition lists correctly. The blank line ensures consistent rendering across HTML, PDF, and EPUB outputs.

**Use cases**:

- rincian, list definitions
- Key terms in chapters
- Parameter descriptions
- Option explanations

## CPMK Alignment

Always tag content with relevant CPMK:
- **CPMK-1**: Foundational Understanding (Ch 1-3)
- **CPMK-2**: Implementation Skills (Ch 4-8)
- **CPMK-3**: Security Analysis (Ch 5, 6, 9, 10, 14)
- **CPMK-4**: Practical Application (Ch 9-10)
- **CPMK-5**: Advanced Awareness (Ch 11-13)

## Depth Indicators

Use star ratings for topic depth:
- ⭐⭐⭐⭐⭐ Core Mastery (must know thoroughly)
- ⭐⭐⭐⭐ Deep Understanding (important)
- ⭐⭐⭐ Solid Knowledge (working understanding)
- ⭐⭐ Awareness (concepts, not details)
- ⭐ Survey (brief exposure)

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Chapters | `XX-topic-name.qmd` | `04-rsa-foundation.qmd` |
| Labs | `labXX-topic.qmd` | `lab04-rsa-scratch.qmd` |
| Images | `chXX-figYY-desc.png` | `ch04-fig03-rsa-flow.png` |
| Code | `descriptive_name.py` | `rsa_implementation.py` |

## Common Workflows

### Creating a New Diagram

**Step 1: Choose Template**
```bash
# For algorithm flowchart
cp images/templates/mermaid-flowchart-template.mmd images/chapters/ch04/

# For protocol sequence
cp images/templates/mermaid-sequence-template.mmd images/chapters/ch06/

# For performance chart
cp images/templates/matplotlib-bar-chart-template.py images/chapters/ch04/
```

**Step 2: Rename Properly**
```bash
# Format: chXX-figYY-description.ext
mv mermaid-flowchart-template.mmd ch04-fig01-rsa-keygen.mmd
```

**Step 3: Edit Content**
- Apply official color palette
- Add clear labels
- Follow best practices (see DIAGRAM_STANDARDS.md)

**Step 4: Use in Chapter**
````markdown
```{mermaid}
%%| label: fig-rsa-keygen
%%| fig-cap: "RSA Key Generation Process showing steps from prime selection to key pair output"
%%| fig-alt: "Flowchart with 7 steps: select primes p and q, compute n, compute phi, select e, compute d, output public key (e,n) and private key (d,n)"
%%| file: images/chapters/ch04/ch04-fig01-rsa-keygen.mmd
```
````

**Step 5: Test**
```bash
# Preview to check rendering
quarto preview chapters/04-rsa-foundation.qmd
```

### Creating a New Chapter

1. Copy template: `cp chapters/_chapter-template.qmd chapters/XX-topic-name.qmd`
2. Update YAML front matter
3. Fill in Learning Objectives with CPMK alignment
4. Write content following structure
5. Add diagrams using workflow above
6. Add to `_quarto.yml`
7. Test build

### Creating a New Lab

1. Copy template: `cp labs/_lab-template.qmd labs/labXX-topic.qmd`
2. Fill overview table
3. Write step-by-step instructions
4. Add checkpoints after each part
5. Create answer key (separate file)
6. Test all code blocks
7. Add to `_quarto.yml`

## Build Commands

```bash
# Preview HTML (with live reload)
quarto preview

# Render all formats
quarto render

# Render specific format
quarto render --to html
quarto render --to pdf

# Render specific file
quarto render chapters/04-rsa-foundation.qmd

# Check for issues
quarto check

# Clean build cache
quarto clean
```

## Quality Checklist

### For All Content
Before committing any content:
- [ ] All code blocks execute without errors
- [ ] Cross-references work (`@fig-`, `@tbl-`, `@sec-`)
- [ ] CPMK alignment noted
- [ ] Indonesian spelling/grammar checked
- [ ] No broken links

### For Diagrams (Additional)
- [ ] Follows naming: `chXX-figYY-description.ext`
- [ ] Uses official color palette (see Diagram Standards)
- [ ] Has `fig-cap` (descriptive caption)
- [ ] Has `fig-alt` (accessibility description)
- [ ] Source file saved (`.mmd`, `.py`)
- [ ] PNG at 300 DPI minimum
- [ ] Tested in both HTML and PDF output
- [ ] Consistent style with other chapter diagrams

### For Python Code
- [ ] PEP 8 compliant
- [ ] Type hints included
- [ ] Docstrings for all functions
- [ ] Executes without errors
- [ ] Uses `cryptography` library for production code

## Key Files Reference

### Core Documentation
- **RPS v3.0**: `../RPS_RK222_KRIPTOGRAFI_ASIMETRIK_v3.0.md`
- **Masterplan**: `MASTERPLAN.md`
- **Development Log**: `DEVELOPMENT_LOG.md` (if exists)

### Diagram Standards
- **Complete Guide**: `DIAGRAM_STANDARDS.md` (~40 pages)
- **Quick Reference**: `DIAGRAM_QUICK_REFERENCE.md` (3 pages)
- **Summary**: `DIAGRAM_STANDARDS_SUMMARY.md` (5 pages)

### Templates
- **Chapter Template**: `chapters/_chapter-template.qmd`
- **Lab Template**: `labs/_lab-template.qmd`
- **Diagram Templates**: `images/templates/`

## Contact

For questions about this project, refer to the MASTERPLAN.md or RPS v3.0 documentation.
