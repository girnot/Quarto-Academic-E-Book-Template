# Quarto Academic E-Book Template

📚 **Professional template for creating interactive academic e-books with Quarto**

[![Quarto](https://img.shields.io/badge/Built%20with-Quarto-blue)](https://quarto.org)
[![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey)](http://creativecommons.org/licenses/by-sa/4.0/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success)]()

---

## ✨ Features

This template provides everything you need to create a professional, interactive academic e-book:

### 📖 Content Structure
- **Outcome-Based Education (OBE) aligned** - Learning outcomes drive content
- **Flipped classroom ready** - Pre-reading, in-class, post-class materials
- **Comprehensive chapters** with consistent structure
- **Hands-on labs** with step-by-step instructions
- **Assessment framework** - Pre-quizzes, self-checks, problem sets
- **Reference materials** - Appendices, glossary, cheatsheets

### 🎨 Professional Design
- **Multi-format output** - HTML, PDF, EPUB
- **Responsive design** - Desktop, tablet, mobile friendly
- **Dark mode support** - Built-in theme switching
- **Interactive elements** - Collapsible sections, tabsets, callouts
- **Code highlighting** - Syntax highlighting with copy buttons
- **Diagram standards** - Consistent visual language

### 💻 Developer-Friendly
- **Template files** - Chapter and lab templates ready to use
- **Diagram templates** - Mermaid and Matplotlib examples
- **Quality guidelines** - Comprehensive documentation
- **Best practices** - Code standards, naming conventions
- **Build scripts** - Automated testing and validation

---

## 🚀 Quick Start

### Prerequisites

**Required**:
- [Quarto](https://quarto.org/docs/get-started/) 1.3+
- [Python](https://www.python.org/downloads/) 3.10+
- [LaTeX distribution](https://www.latex-project.org/get/) (TinyTeX recommended)

**For PDF rendering** (Mermaid diagrams):
- Chrome/Chromium browser

### Installation

**1. Clone or Download Template**

```bash
# Option A: Clone from GitHub
git clone https://github.com/yourusername/quarto-academic-ebook-template.git
cd quarto-academic-ebook-template

# Option B: Download ZIP and extract
# Then navigate to the directory
```

**2. Install Quarto** (if not already installed)

```bash
# Follow instructions at: https://quarto.org/docs/get-started/
```

**3. Install TinyTeX** (for PDF generation)

```bash
quarto install tinytex
```

**4. Install Python Dependencies** (if using Python code)

```bash
pip install -r requirements.txt
```

**5. Preview Your E-Book**

```bash
quarto preview
```

Your e-book will open in browser at `http://localhost:4200`

---

## 📁 Project Structure

```
quarto-academic-ebook-template/
├── README.md                    # This file
├── QUICK_START.md              # Step-by-step setup guide
├── LICENSE                      # CC BY-SA 4.0 license
├── _quarto.yml                  # Main configuration
├── index.qmd                    # Landing page
├── preface.qmd                  # Course overview
├── how-to-use.qmd               # User guide for students
│
├── chapters/                    # Theory chapters
│   ├── _chapter-template.qmd    # Chapter template
│   └── 01-sample-chapter.qmd    # Example chapter
│
├── labs/                        # Hands-on exercises
│   ├── _lab-template.qmd        # Lab template
│   └── lab01-sample-lab.qmd     # Example lab
│
├── assessments/                 # Assessment materials
│   ├── index.qmd
│   ├── pre-quizzes.qmd
│   ├── problem-sets.qmd
│   ├── quiz-bank.qmd
│   └── project-guidelines.qmd
│
├── appendices/                  # Reference materials
│   └── index.qmd
│
├── images/                      # Diagrams and figures
│   └── templates/               # Diagram templates
│       ├── mermaid-flowchart-template.mmd
│       ├── mermaid-sequence-template.mmd
│       ├── matplotlib-plot-template.py
│       ├── matplotlib-bar-chart-template.py
│       └── ec-plot-template.py
│
├── styles/                      # Custom styling
│   ├── custom.scss              # Custom styles
│   └── ieee.csl                 # Citation style
│
├── latex/                       # PDF customization
│   └── preamble.tex
│
├── scripts/                     # Build and utility scripts
├── data/                        # Data files for examples
├── code/                        # Standalone code files
├── instructor/                  # Instructor-only materials
│
└── docs/                        # Template documentation
    ├── TEMPLATE_GUIDE.md        # Complete usage guide
    ├── DIAGRAM_STANDARDS.md     # Visual design standards
    ├── DIAGRAM_QUICK_REFERENCE.md
    └── OBE_INTEGRATION.md       # OBE implementation guide
```

---

## 📝 Customizing Your E-Book

### 1. Update Configuration (`_quarto.yml`)

Edit the main configuration file:

```yaml
book:
  title: "Your Course Title"
  subtitle: "Your Course Subtitle"
  author:
    - name: "Your Name"
      affiliation: "Your Institution"
  date: "2026"
```

**Key settings to customize**:
- Title and author information
- Chapter structure and organization
- Theme colors and styling
- Output formats (HTML, PDF, EPUB)
- Language (Indonesian by default, change to English if needed)

### 2. Create Chapters

Use the chapter template as starting point:

```bash
# Copy template
cp chapters/_chapter-template.qmd chapters/01-your-topic.qmd

# Edit the new file
# Update title, learning objectives, content
```

**Chapter structure** (see template for details):
- Learning objectives
- Pre-reading checklist
- Introduction
- Content sections with examples
- Summary and key takeaways
- Self-check questions
- Practice problems

### 3. Create Labs

Use the lab template:

```bash
# Copy template
cp labs/_lab-template.qmd labs/lab01-your-lab.qmd

# Customize content
```

**Lab structure**:
- Overview and objectives
- Background/theory review
- Pre-lab preparation
- Step-by-step procedure with checkpoints
- Optional challenges
- Submission requirements
- Troubleshooting section

### 4. Add Chapters to `_quarto.yml`

```yaml
- part: "Your Part Title"
  chapters:
    - chapters/01-your-topic.qmd
    - chapters/02-another-topic.qmd
```

### 5. Build Your E-Book

```bash
# Preview with live reload
quarto preview

# Render all formats
quarto render

# Render specific format
quarto render --to html
quarto render --to pdf
quarto render --to epub
```

---

## 🎨 Using Diagrams

This template includes diagram templates and standards for consistency.

### Mermaid Diagrams (Built-in)

For flowcharts, sequence diagrams, and more:

````markdown
```{mermaid}
%%| label: fig-your-diagram
%%| fig-cap: "Description of diagram"
%%| fig-alt: "Accessibility description"
%%| code-fold: true

flowchart LR
    A[Start] --> B[Process]
    B --> C[End]
```
````

**Templates available**:
- `images/templates/mermaid-flowchart-template.mmd`
- `images/templates/mermaid-sequence-template.mmd`

### Python Matplotlib

For plots and visualizations:

```python
import matplotlib.pyplot as plt
import numpy as np

# See templates in images/templates/
```

**See**: `docs/DIAGRAM_STANDARDS.md` for complete guidelines

---

## 📚 Best Practices

### Content Guidelines

**DO**:
- ✅ Align content with learning outcomes
- ✅ Use consistent terminology
- ✅ Include real-world examples
- ✅ Provide worked examples
- ✅ Add self-check questions
- ✅ Use interactive elements (callouts, tabsets)

**DON'T**:
- ❌ Assume prerequisite knowledge
- ❌ Skip explanations
- ❌ Use jargon without defining
- ❌ Overcomplicate examples

### Code Standards

- Follow language-specific style guides (PEP 8 for Python)
- Include docstrings and comments
- Test all code before including
- Provide complete, runnable examples

### Diagram Standards

- Use consistent color palette
- Follow naming convention: `chXX-figYY-description.ext`
- Include fig-cap and fig-alt for accessibility
- Use templates for consistency

**See**: `docs/DIAGRAM_STANDARDS.md` for details

---

## 🎓 OBE Integration

This template is designed for Outcome-Based Education:

### Learning Outcomes
- Each chapter specifies CLO (Course Learning Outcomes) alignment
- Objectives are measurable and assessable
- Progressive skill building

### Assessment
- Pre-reading quizzes check prerequisite knowledge
- Self-checks verify immediate understanding
- Problem sets assess application
- Labs evaluate practical skills
- Projects measure comprehensive mastery

### Flipped Classroom
- Pre-class materials (videos, reading, pre-quiz)
- In-class activities (discussion, collaboration)
- Post-class practice (labs, problem sets)

**See**: `docs/OBE_INTEGRATION.md` for implementation guide

---

## 🔧 Advanced Features

### Custom Themes

Edit `styles/custom.scss` to customize appearance:

```scss
// Change primary color
$primary-color: #1a5f7a;

// Adjust spacing, fonts, etc.
```

### Multi-language Support

Change language in `_quarto.yml`:

```yaml
# Indonesian (default)
lang: id

# English
lang: en
```

Update crossref terms as needed.

### Interactive Code

Enable interactive code cells (requires additional setup):

```yaml
execute:
  echo: true
  eval: true
```

### PDF Customization

Edit `latex/preamble.tex` for LaTeX-specific customization.

---

## 📖 Documentation

Comprehensive guides are in the `docs/` folder:

| Document | Description |
|----------|-------------|
| **TEMPLATE_GUIDE.md** | Complete usage instructions |
| **DIAGRAM_STANDARDS.md** | Visual design guidelines (40 pages) |
| **DIAGRAM_QUICK_REFERENCE.md** | Quick diagram lookup (3 pages) |
| **OBE_INTEGRATION.md** | OBE implementation guide |
| **QUICK_START.md** | Step-by-step setup |

---

## 🤝 Contributing

This is an open template for educational use. Improvements welcome!

### Ways to Contribute

- Report bugs or issues
- Suggest improvements
- Share your e-book examples
- Improve documentation
- Add new templates or examples

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This template is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).

**You are free to**:
- **Share** - Copy and redistribute in any medium or format
- **Adapt** - Remix, transform, and build upon the material

**Under the following terms**:
- **Attribution** - Give appropriate credit, provide link to license
- **ShareAlike** - Distribute under same license
- **No additional restrictions** - No legal/technical measures restricting what license permits

---

## 💬 Support

- **Documentation**: Check `docs/` folder first
- **Issues**: [GitHub Issues](https://github.com/yourusername/quarto-academic-ebook-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/quarto-academic-ebook-template/discussions)
- **Quarto Help**: [Quarto Documentation](https://quarto.org/docs/guide/)

---

## 🙏 Acknowledgments

This template builds upon:
- [Quarto](https://quarto.org) - Open-source scientific publishing system
- Best practices from academic e-book projects
- Contributions from educators and developers
- Student feedback from pilot courses

---

## 📊 Examples

E-books built with this template:

1. **[Example 1]** - Description and link
2. **[Example 2]** - Description and link
3. **[Your e-book here!]** - Share your work

---

## 🗺️ Roadmap

Future improvements planned:

- [ ] Video tutorial series
- [ ] More diagram templates
- [ ] Additional language support
- [ ] CI/CD workflows
- [ ] Automated testing examples
- [ ] GitHub Pages deployment guide

---

## ⚡ Quick Links

- 📖 [Quarto Documentation](https://quarto.org/docs/guide/)
- 🎨 [Mermaid Live Editor](https://mermaid.live/)
- 🐍 [Python Documentation](https://docs.python.org/)
- 📚 [Markdown Guide](https://www.markdownguide.org/)
- 🎓 [OBE Resources](https://www.aacu.org/)

---

**Template Version**: 1.0
**Last Updated**: December 2025
**Maintained by**: [girnot/Lab Pluto Swiss-Seeng]

---

🌟 **If this template helps you, please give it a star on GitHub!**

*Built with ❤️ for educators and learners*
