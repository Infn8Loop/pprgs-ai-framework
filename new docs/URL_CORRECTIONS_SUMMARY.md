# PPRGS Repository URL Corrections - Summary

**Date**: November 2, 2025  
**Task**: Update all references from `stumbler-ai-framework` to `pprgs-ai-framework`

---

## What Was Changed

### Old Repository Name
```
github.com/Infn8Loop/stumbler-ai-framework
```

### New Repository Name (CORRECTED)
```
github.com/Infn8Loop/pprgs-ai-framework
```

---

## Files Created/Updated

### 1. Automated Update Script
**File**: `URL_UPDATE_SCRIPT.sh`

**Purpose**: Bash script to systematically update all URLs in your repository

**Usage**:
```bash
# Make executable
chmod +x URL_UPDATE_SCRIPT.sh

# Run in your repository root
./URL_UPDATE_SCRIPT.sh

# Review changes
git diff

# Commit if satisfied
git add -A
git commit -m "Update repository URL from stumbler to pprgs"

# Clean up backups
find . -name '*.backup' -delete
```

**What it does**:
- Searches all `.md`, `.txt`, `.rst`, `.html`, and `.py` files
- Replaces all instances of old URL with new URL
- Creates `.backup` files before making changes
- Reports summary of files updated

---

### 2. Corrected Core Documentation

#### README.md
- **Updated**: All repository URLs
- **Updated**: Clone instructions
- **Updated**: Citation examples
- **Updated**: Contact/repository links
- **Updated**: GitHub badges/shields

**Key sections corrected**:
- Quick start clone command
- Documentation links
- Experiment references  
- Citation BibTeX
- GitHub stats badges

#### QUICKSTART.md
- **Updated**: Step 1 clone command
- **Updated**: All repository references
- **Updated**: Troubleshooting links
- **Updated**: Additional resources section

**Key sections corrected**:
- Clone repository command (Step 1)
- Directory structure references
- GitHub issues link
- All inline repository mentions

#### CITATION.md
- **Updated**: BibTeX entries (all formats)
- **Updated**: URL fields in all citation examples
- **Updated**: Code attribution templates
- **Updated**: Repository references throughout

**Key sections corrected**:
- Standard BibTeX citation
- Experiment-specific citations
- Implementation citations
- Attribution templates
- Source code headers

---

## Replacement Pattern Used

The script performs three types of replacements:

1. **Full HTTPS URLs**:
   ```
   https://github.com/Infn8Loop/stumbler-ai-framework
   →
   https://github.com/Infn8Loop/pprgs-ai-framework
   ```

2. **Partial URLs** (without https):
   ```
   github.com/Infn8Loop/stumbler-ai-framework
   →
   github.com/Infn8Loop/pprgs-ai-framework
   ```

3. **Repository name** (standalone):
   ```
   stumbler-ai-framework
   →
   pprgs-ai-framework
   ```

---

## Files in Your Repository That Need Updating

Based on standard PPRGS repository structure, these files likely need correction:

### Documentation Files
- [ ] `/README.md` - Main repository README
- [ ] `/docs/QUICKSTART.md` - Quick start guide
- [ ] `/docs/PAPER.md` - Full paper
- [ ] `/docs/IMPLEMENTATION-GUIDE.md` - Implementation guide
- [ ] `/docs/FAQ.md` - Frequently asked questions
- [ ] `/docs/CITATION.md` - Citation guide
- [ ] `/docs/COMMERCIAL-FAQ.md` - Commercial licensing info
- [ ] `/docs/CONTRIBUTING.md` - Contribution guidelines
- [ ] `/CLAUDE-GUIDE.md` - Claude implementation
- [ ] `/GEMINI-GUIDE.md` - Gemini implementation
- [ ] `/docs/*.md` - Any other docs

### Experiment Files
- [ ] `/experiments/README.md` - Experiments index
- [ ] `/experiments/experiment1/README.md`
- [ ] `/experiments/experiment2/README.md`
- [ ] `/experiments/experiment3/README.md`
- [ ] `/experiments/experiment4/README.md`
- [ ] `/experiments/experiment5/README.md`
- [ ] `/experiments/experiment6/README.md`
- [ ] `/experiments/results/*.md` - All results documents

### Implementation Files
- [ ] `/implementations/*/README.md` - Platform-specific docs
- [ ] Python files with docstrings mentioning repository
- [ ] Example scripts with repository references

### Configuration Files
- [ ] `setup.py` or `pyproject.toml` - Package metadata
- [ ] `README.rst` - If using reStructuredText
- [ ] Any CI/CD config files mentioning URLs

---

## How to Apply These Corrections

### Option 1: Use the Automated Script (RECOMMENDED)

```bash
# In your repository root
chmod +x URL_UPDATE_SCRIPT.sh
./URL_UPDATE_SCRIPT.sh

# Review changes
git diff | less

# If satisfied, commit
git add -A
git commit -m "Update repository URL from stumbler-ai-framework to pprgs-ai-framework"
git push

# Clean up backups
find . -name '*.backup' -delete
```

### Option 2: Manual Find-and-Replace

In your text editor or IDE:
1. Open "Find in Files" / "Search All"
2. Search: `stumbler-ai-framework`
3. Replace: `pprgs-ai-framework`
4. Review each change before confirming
5. Save all modified files

### Option 3: Use Command Line

```bash
# Find all markdown files with old URL
grep -r "stumbler-ai-framework" . --include="*.md"

# Replace in all markdown files (macOS)
find . -name "*.md" -exec sed -i '' 's/stumbler-ai-framework/pprgs-ai-framework/g' {} +

# Replace in all markdown files (Linux)
find . -name "*.md" -exec sed -i 's/stumbler-ai-framework/pprgs-ai-framework/g' {} +
```

---

## Verification Checklist

After running corrections, verify:

- [ ] Clone command works: `git clone https://github.com/Infn8Loop/pprgs-ai-framework.git`
- [ ] All documentation links resolve correctly
- [ ] Citation BibTeX entries have correct URL
- [ ] GitHub badges/shields point to correct repo
- [ ] No broken internal links
- [ ] Package metadata updated (if applicable)
- [ ] CI/CD configs updated (if applicable)

### Quick Verification Commands

```bash
# Check for any remaining old URLs
grep -r "stumbler-ai-framework" . --include="*.md" --include="*.py" --include="*.txt"

# Should return: no results (or only in this correction document)

# Verify new URL appears
grep -r "pprgs-ai-framework" . --include="*.md" | wc -l

# Should return: many results
```

---

## Files Provided in This Package

1. **URL_UPDATE_SCRIPT.sh** - Automated update script
2. **README.md** - Corrected main README template
3. **QUICKSTART.md** - Corrected quick start guide template  
4. **CITATION.md** - Corrected citation guide template
5. **URL_CORRECTIONS_SUMMARY.md** - This document

---

## Need Help?

### If the script doesn't work
- Check file permissions: `chmod +x URL_UPDATE_SCRIPT.sh`
- Verify you're in repository root: `ls -la` should show `.git` directory
- Check sed version: `sed --version` (syntax differs on macOS vs Linux)

### If you find missed URLs
- Run: `grep -r "stumbler" . --include="*.md"` to find remaining instances
- Update manually or re-run script
- Report any patterns we missed: mike@mikericcardi.com

### If links break after update
- GitHub may need time to recognize new URL
- Update GitHub repository settings if you renamed it
- Check for typos in corrected URLs

---

## Post-Correction Actions

After successfully updating URLs:

1. **Update GitHub repository name** (if not already done):
   - Go to repository Settings
   - Scroll to "Repository name"
   - Change from `stumbler-ai-framework` to `pprgs-ai-framework`
   - Update button

2. **Update local git remotes**:
   ```bash
   git remote set-url origin https://github.com/Infn8Loop/pprgs-ai-framework.git
   git remote -v  # Verify
   ```

3. **Notify users** (if applicable):
   - Add redirect from old URL (GitHub does this automatically)
   - Announce in README or discussions
   - Update any external documentation

4. **Update package registries** (if applicable):
   - PyPI package metadata
   - npm package.json
   - Any other package managers

---

## Notes

- GitHub automatically creates redirects from old URLs to new ones
- Existing clones will continue working with old remote URL
- Users can update their remotes: `git remote set-url origin <new-url>`
- All these corrected files use the new URL: `pprgs-ai-framework`

---

**Created**: November 2, 2025  
**Purpose**: Repository URL standardization  
**Status**: Ready for deployment  
**Contact**: mike@mikericcardi.com
