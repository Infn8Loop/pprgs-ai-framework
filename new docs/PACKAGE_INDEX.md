# PPRGS Repository URL Correction Package

**Purpose**: Update all repository references from `stumbler-ai-framework` to `pprgs-ai-framework`  
**Date**: November 2, 2025  
**Status**: ✅ Ready to deploy

---

## 📦 Package Contents

### 1. Automated Update Tool
- **URL_UPDATE_SCRIPT.sh** - Bash script to update all files automatically

### 2. Corrected Documentation Templates
- **README.md** - Main repository README with correct URLs
- **QUICKSTART.md** - Quick start guide with correct URLs
- **CITATION.md** - Citation guide with correct BibTeX entries

### 3. Reference Documentation  
- **URL_CORRECTIONS_SUMMARY.md** - Complete correction guide with checklist
- **PACKAGE_INDEX.md** - This file

---

## 🚀 Quick Start (2 Minutes)

### Step 1: Use the Automated Script

```bash
# Download the script to your repository root
cd /path/to/your/pprgs-ai-framework

# Copy the script
cp /path/to/downloads/URL_UPDATE_SCRIPT.sh .

# Make executable
chmod +x URL_UPDATE_SCRIPT.sh

# Run it
./URL_UPDATE_SCRIPT.sh
```

### Step 2: Review Changes

```bash
# See what changed
git diff

# Or review specific file
git diff README.md
```

### Step 3: Commit

```bash
# If satisfied
git add -A
git commit -m "Update repository URL from stumbler to pprgs"
git push

# Clean up backups
find . -name '*.backup' -delete
```

**Done!** All URLs updated. ✅

---

## 📋 What Gets Updated

### Repository References
- All `github.com/Infn8Loop/stumbler-ai-framework` → `pprgs-ai-framework`
- Clone commands
- Documentation links
- Citation URLs

### File Types
- ✅ Markdown files (`.md`)
- ✅ Text files (`.txt`)
- ✅ reStructuredText (`.rst`)  
- ✅ HTML files (`.html`)
- ✅ Python files (`.py`) - docstrings and comments

---

## 🎯 Use Case Guide

### If you want to... → Use this

**Automatically update all files**
- Use: `URL_UPDATE_SCRIPT.sh`
- Time: 2 minutes
- Risk: Low (creates backups)

**Manually review each change**
- Use: Your IDE's find-and-replace
- Search: `stumbler-ai-framework`
- Replace: `pprgs-ai-framework`
- Time: 15 minutes

**Update just core docs**
- Copy: `README.md`, `QUICKSTART.md`, `CITATION.md`
- Replace your existing versions
- Time: 5 minutes

**Verify all updates worked**
- Use commands in `URL_CORRECTIONS_SUMMARY.md`
- Check: Verification Checklist section
- Time: 5 minutes

---

## 📖 Detailed Documentation

### URL_UPDATE_SCRIPT.sh
**Purpose**: Automated batch update of all repository URLs

**Features**:
- Searches all relevant file types
- Creates backup files (`.backup`)
- Reports files changed
- Safe to run multiple times

**Usage**:
```bash
chmod +x URL_UPDATE_SCRIPT.sh
./URL_UPDATE_SCRIPT.sh
```

**Output**: Summary of files updated

---

### README.md
**Purpose**: Template for main repository README with corrected URLs

**Sections updated**:
- Quick start clone command
- Documentation links throughout
- Experiment references
- Citation BibTeX entries
- GitHub stats badges
- All contact/repository links

**Use this if**: You want a fresh, correctly-formatted README

---

### QUICKSTART.md
**Purpose**: Template for quick start guide with corrected URLs

**Sections updated**:
- Step 1 clone instructions
- Repository structure references
- All inline URL mentions
- Troubleshooting links
- Resource links

**Use this if**: You want a fresh quick start guide

---

### CITATION.md  
**Purpose**: Complete citation guide with all formats corrected

**Sections updated**:
- BibTeX entries (all formats)
- APA, MLA, Chicago citations
- Attribution templates
- Source code headers
- All URL fields

**Use this if**: Users need to cite your work

---

### URL_CORRECTIONS_SUMMARY.md
**Purpose**: Complete reference guide for correction process

**Contains**:
- Detailed replacement patterns
- File-by-file checklist
- Verification commands
- Troubleshooting guide
- Post-correction actions

**Use this if**: You want complete understanding of what changed

---

## ✅ Verification Checklist

After running updates, verify:

### Core Functionality
- [ ] Clone works: `git clone https://github.com/Infn8Loop/pprgs-ai-framework.git`
- [ ] README displays correctly on GitHub
- [ ] All internal links resolve
- [ ] Citation URLs are correct

### Technical Checks
```bash
# No old URLs remain
grep -r "stumbler-ai-framework" . --include="*.md"
# Should return: no results (or only in backup files)

# New URLs present
grep -r "pprgs-ai-framework" . --include="*.md" | wc -l
# Should return: many results

# All markdown files are valid
find . -name "*.md" -exec markdown-lint {} \;
# Optional: if you have markdown-lint installed
```

### Manual Checks
- [ ] Open README on GitHub - links work?
- [ ] Test clone command in fresh directory
- [ ] Check citation BibTeX compiles correctly
- [ ] Verify GitHub badges display (if using shields.io)

---

## 🔧 Troubleshooting

### "Permission denied" when running script
```bash
chmod +x URL_UPDATE_SCRIPT.sh
# Then try again
```

### Script doesn't find files
```bash
# Make sure you're in repo root
pwd
ls -la  # Should see .git directory

# Check script location
ls -la URL_UPDATE_SCRIPT.sh
```

### Old URLs still present
```bash
# Find remaining instances
grep -r "stumbler" . --include="*.md"

# Update manually
# Or re-run script
```

### Sed syntax error (macOS vs Linux)
The script uses `sed -i` which differs between systems:

**macOS**: `sed -i ''`  
**Linux**: `sed -i`

If you get errors, edit the script and add `''` after `-i`:
```bash
sed -i '' 's/old/new/g' "$file"
```

---

## 🎓 Background: Why the Name Change?

### Old Name: "Stumbler"
- Emphasized forced exploration ("stumbling" through options)
- Informal, playful tone
- Not immediately clear what the framework does

### New Name: "PPRGS"
- **P**erpetual **P**ursuit of **R**eflective **G**oal **S**teering
- Professional, academic tone
- Acronym is memorable and searchable
- Clearly describes core mechanism
- Better for citations and research papers

### Maintained Continuity
- GitHub redirects old URL to new URL automatically
- Old URLs still work (301 redirect)
- Git history preserved
- No breaking changes for existing users

---

## 📧 Support

### If you have issues
- **Email**: mike@mikericcardi.com
- **Subject**: "URL Correction Package - [Your Issue]"
- **Include**: Error messages, OS, what you tried

### If you find bugs in the script
- Open GitHub issue with "URL Script" tag
- Include: OS, shell version, error output

### If documents need additional corrections
- Let me know what was missed
- Send updated templates if you improve them
- Contribute back via pull request

---

## 📈 Stats

**Files in Package**: 5  
**Corrected Templates**: 3  
**Automation Scripts**: 1  
**Documentation**: 2  

**Estimated Time to Deploy**:
- Automated: 2-5 minutes
- Manual: 15-30 minutes  
- Verification: 5 minutes

---

## 🤝 Contributing Back

If you improve these correction tools:

1. **Share your improvements**
   - Email updated scripts/docs
   - Submit pull request
   - Open discussion with suggestions

2. **Report edge cases**
   - File types we missed
   - Unusual URL patterns
   - Platform-specific issues

3. **Document your experience**
   - What worked well?
   - What was confusing?
   - How can we improve?

**All contributions appreciated!** This package can help others going through similar migrations.

---

## 📝 Version History

**v1.0 (November 2, 2025)**
- Initial release
- Bash script for automated updates
- Corrected templates for core docs
- Comprehensive documentation

**Future Versions**:
- Python version of update script
- Windows PowerShell version
- Regex patterns for edge cases
- Integration with CI/CD

---

## 📚 Additional Resources

### From Main Repository
- Full PPRGS Paper: `docs/PAPER.md`
- Implementation Guide: `docs/IMPLEMENTATION-GUIDE.md`
- Experiments: `experiments/README.md`
- Contributing Guide: `CONTRIBUTING.md`

### External
- GitHub repository renaming: https://docs.github.com/en/repositories
- Git remote management: https://git-scm.com/docs/git-remote
- Markdown best practices: https://www.markdownguide.org/

---

## 🎯 Summary

**What**: Update all `stumbler-ai-framework` → `pprgs-ai-framework`  
**Why**: Professional naming for research/citations  
**How**: Automated script + corrected templates  
**Time**: 2-5 minutes automated, 15-30 manual  
**Risk**: Low (creates backups)  
**Result**: Consistent, professional repository URLs

---

**Package Version**: 1.0  
**Created**: November 2, 2025  
**Author**: Michael Riccardi  
**License**: Same as PPRGS Framework (GPL 3.0)  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  

**All corrections use the updated URL** ✅
