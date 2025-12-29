# Quick Start Guide

Get your academic e-book up and running in 15 minutes!

## ⚡ Fast Track (TL;DR)

```bash
# 1. Install Quarto (if needed)
# Download from: https://quarto.org/docs/get-started/

# 2. Clone template
git clone https://github.com/yourusername/quarto-academic-ebook-template.git my-ebook
cd my-ebook

# 3. Customize
# Edit _quarto.yml with your course info

# 4. Preview
quarto preview
```

Done! Your e-book is running at `http://localhost:4200`

---

## 📋 Detailed Setup

### Step 1: Install Prerequisites (10 minutes)

#### 1.1 Install Quarto

**Windows**:
1. Download installer from [quarto.org](https://quarto.org/docs/get-started/)
2. Run the installer
3. Verify: Open PowerShell and run `quarto --version`

**macOS**:
```bash
# Using Homebrew
brew install quarto

# Or download from quarto.org
```

**Linux**:
```bash
# Download and install
sudo wget https://quarto.org/download/latest/quarto-linux-amd64.deb
sudo dpkg -i quarto-linux-amd64.deb

# Verify
quarto --version
```

#### 1.2 Install Python (if using code examples)

Download from [python.org](https://www.python.org/downloads/) - Get Python 3.10+

Verify:
```bash
python --version  # or python3 --version
```

#### 1.3 Install LaTeX (for PDF output)

**Easiest method** - Use TinyTeX via Quarto:
```bash
quarto install tinytex
```

**Alternative** - Full LaTeX distribution:
- Windows: [MiKTeX](https://miktex.org/)
- macOS: [MacTeX](https://www.tug.org/mactex/)
- Linux: TeX Live (`sudo apt install texlive-full`)

---

### Step 2: Get the Template (2 minutes)

**Option A: Clone with Git**
```bash
git clone https://github.com/yourusername/quarto-academic-ebook-template.git my-course-ebook
cd my-course-ebook
```

**Option B: Download ZIP**
1. Go to GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract to your working directory
4. Navigate to the folder in terminal

---

### Step 3: Customize Configuration (5 minutes)

Edit `_quarto.yml`:

```yaml
book:
  title: "Introduction to Data Science"        # ← Change this
  subtitle: "A Hands-on Approach"              # ← Change this
  author:
    - name: "Dr. Jane Smith"                   # ← Your name
      affiliation: "University of Example"      # ← Your institution
  date: "2026"

  page-footer:
    left: |
      Data Science Department                   # ← Your department
    right: |
      DS101 - Introduction to Data Science      # ← Course code/name
```

Update language if needed:
```yaml
# Keep as 'id' for Indonesian, change to 'en' for English
lang: id
```

---

### Step 4: Preview Your E-Book (1 minute)

```bash
quarto preview
```

Your browser will open to `http://localhost:4200` showing your e-book!

**Tip**: Leave this running - it auto-reloads when you edit files.

---

### Step 5: Add Your Content (ongoing)

#### Create First Chapter

```bash
# Copy the template
cp chapters/_chapter-template.qmd chapters/01-introduction.qmd
```

Edit `chapters/01-introduction.qmd`:
- Change the title
- Update learning objectives
- Add your content

Add to `_quarto.yml`:
```yaml
- part: "Part I: Fundamentals"
  chapters:
    - chapters/01-introduction.qmd  # ← Add this line
```

Save and watch it appear in your preview!

#### Create First Lab

```bash
# Copy the template
cp labs/_lab-template.qmd labs/lab01-getting-started.qmd
```

Edit `labs/lab01-getting-started.qmd` and add to `_quarto.yml`:
```yaml
- part: "Labs"
  chapters:
    - labs/index.qmd
    - labs/lab01-getting-started.qmd  # ← Add this
```

---

## 🎨 Quick Customization Tips

### Change Theme Colors

Edit `styles/custom.scss`:

```scss
/* Change primary color */
$primary-color: #1a5f7a;  /* Your color here */
```

### Add Images

```bash
# Put images in images/ folder
images/
  ├── cover.png          # E-book cover
  ├── logo.png           # Institution logo
  └── chapters/
      └── ch01/
          └── diagram.png
```

Reference in content:
```markdown
![Caption text](images/chapters/ch01/diagram.png)
```

### Add Code Examples

````markdown
```python
def hello_world():
    print("Hello from your e-book!")

hello_world()
```
````

---

## 📖 Build Output Formats

### HTML (Default - always works)

```bash
quarto render --to html
```
Output: `_book/index.html`

### PDF (requires LaTeX)

**Windows** (for Mermaid diagrams):
```powershell
# Must run in Windows PowerShell, not WSL
quarto render --to pdf
```

**macOS/Linux**:
```bash
quarto render --to pdf
```

Output: `_book/Your-Book-Title.pdf`

### EPUB (for e-readers)

```bash
quarto render --to epub
```

Output: `_book/Your-Book-Title.epub`

### All Formats at Once

```bash
quarto render
```

---

## 🔧 Common Issues & Solutions

### Issue: `quarto: command not found`

**Solution**: Quarto not in PATH.
- Restart terminal after installation
- Or add to PATH manually

### Issue: Mermaid diagrams don't appear in PDF

**SSolution - Opsi 1**: Chrome path not set correctly.

Edit `_quarto.yml`:
```yaml
pdf:
  mermaid:
    chrome-path: "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Windows
    # chrome-path: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS
    # chrome-path: "/usr/bin/chromium-browser"  # Linux
```

**Solution - Opsi 2**: Create diagrams as images and include them instead (see "Add Images" section). 


### Issue: Python code not executing

it strong recommended to use a virtual environment

**Solution**: Install required packages:
```bash
pip install -r requirements.txt
```

### Issue: PDF build fails with LaTeX errors

**Solution**:
```bash
# Reinstall TinyTeX
quarto uninstall tinytex
quarto install tinytex
```

---

## 📚 Next Steps

### Learn the Template Structure
1. Read `README.md` for overview
2. Check `docs/TEMPLATE_GUIDE.md` for detailed guide
3. Review example chapter: `chapters/01-sample-chapter.qmd`
4. Review example lab: `labs/lab01-sample-lab.qmd`

### Customize Your E-Book
1. Update all placeholder text in `_quarto.yml`
2. Edit `preface.qmd` with course information
3. Customize `how-to-use.qmd` for your students
4. Create chapters using templates
5. Add labs with step-by-step instructions

### Add Assessment Materials
1. Edit `assessments/pre-quizzes.qmd`
2. Create problem sets in `assessments/problem-sets.qmd`
3. Build quiz bank for review
4. Define project guidelines

### Polish and Deploy
1. Test all code examples
2. Review all links and cross-references
3. Build final PDFs
4. Deploy to GitHub Pages (optional)
5. Share with students!

---

## 🎯 Workflow Recommendations

### During Development

```bash
# Keep preview running in one terminal
quarto preview

# Edit files in your preferred editor
# Changes auto-reload in browser
```

### Before Sharing

```bash
# Clean old builds
quarto clean

# Render all formats
quarto render

# Check output in _book/ folder
ls _book/
```

### Version Control

```bash
# Initialize git (if not already)
git init

# Add files
git add .

# Commit
git commit -m "Initial e-book setup"

# Push to GitHub
git remote add origin https://github.com/yourusername/your-ebook.git
git push -u origin main
```

---

## 💡 Pro Tips

1. **Start Small**: Begin with 1-2 chapters, then expand
2. **Use Templates**: Copy and modify, don't start from scratch
3. **Test Early**: Build PDF early to catch formatting issues
4. **Stay Organized**: Use consistent file naming
5. **Version Control**: Commit frequently to track changes
6. **Get Feedback**: Share drafts with colleagues/students

---

## 📞 Getting Help

- **Template Documentation**: Check `docs/` folder
- **Quarto Docs**: [quarto.org/docs](https://quarto.org/docs/)
- **GitHub Issues**: Report bugs or ask questions
- **Community**: Quarto discussions and forums

---

## ✅ Checklist

Before considering your e-book ready:

- [ ] All placeholder text replaced
- [ ] Course information updated in `_quarto.yml`
- [ ] Preface and how-to-use customized
- [ ] At least 3-5 chapters created
- [ ] Labs aligned with chapters
- [ ] Assessment materials prepared
- [ ] All code examples tested
- [ ] Images and diagrams included
- [ ] Cross-references working
- [ ] HTML build successful
- [ ] PDF build successful (if using)
- [ ] EPUB build successful (if using)
- [ ] Spell-check completed
- [ ] Peer review done
- [ ] Student feedback incorporated (if pilot testing)

---

**You're ready to create an amazing academic e-book! 🚀**

*If you get stuck, remember: docs folder has detailed guides for everything.*
