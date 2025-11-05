#!/bin/bash

# PPRGS Repository URL Update Script
# Updates all instances of old repository name to new name
# 
# OLD: github.com/Infn8Loop/stumbler-ai-framework
# NEW: github.com/Infn8Loop/pprgs-ai-framework

echo "🔄 Starting PPRGS repository URL update..."
echo ""

# Function to update URLs in a file
update_file() {
    local file="$1"
    local changes=0
    
    # Check if file contains old URL
    if grep -q "stumbler-ai-framework" "$file"; then
        echo "📝 Updating: $file"
        
        # Create backup
        cp "$file" "$file.backup"
        
        # Perform replacements
        sed -i 's|github\.com/Infn8Loop/stumbler-ai-framework|github.com/Infn8Loop/pprgs-ai-framework|g' "$file"
        sed -i 's|Infn8Loop/stumbler-ai-framework|Infn8Loop/pprgs-ai-framework|g' "$file"
        sed -i 's|stumbler-ai-framework|pprgs-ai-framework|g' "$file"
        
        changes=1
    fi
    
    return $changes
}

# Counter for updated files
total_updated=0

# Find and update all markdown files
echo "Searching for markdown files..."
find . -type f -name "*.md" | while read -r file; do
    if update_file "$file"; then
        ((total_updated++))
    fi
done

# Find and update other common documentation files
echo ""
echo "Searching for other documentation files..."
find . -type f \( -name "*.txt" -o -name "*.rst" -o -name "*.html" \) | while read -r file; do
    if update_file "$file"; then
        ((total_updated++))
    fi
done

# Find and update Python files (for docstrings, comments, etc.)
echo ""
echo "Searching for Python files..."
find . -type f -name "*.py" | while read -r file; do
    if update_file "$file"; then
        ((total_updated++))
    fi
done

echo ""
echo "✅ Update complete!"
echo ""
echo "📊 Summary:"
echo "   - Updated repository name from 'stumbler-ai-framework' to 'pprgs-ai-framework'"
echo "   - Backup files created with .backup extension"
echo ""
echo "⚠️  Important: Review changes before committing!"
echo "   - Check: git diff"
echo "   - Remove backups: find . -name '*.backup' -delete"
echo ""
echo "🎯 Next steps:"
echo "   1. Review the changes: git diff"
echo "   2. Test your documentation links"
echo "   3. Commit: git add -A && git commit -m 'Update repository URL from stumbler to pprgs'"
echo "   4. Clean backups: find . -name '*.backup' -delete"
