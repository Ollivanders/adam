#!/bin/sh
#
# Populates documentation from the docs folder,
# DEPRECATED -----------------------------------------------------------------------------

CUR_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
MAIN_DIRECTORY="$(cd "$(dirname "$CUR_DIRECTORY")" && pwd -P)"

README_FILE=$MAIN_DIRECTORY/README.md
INDEX_FILE=$MAIN_DIRECTORY/INDEX.md
CONTRIBUTING_FILE=$MAIN_DIRECTORY/CONTRIBUTING.md
TROUBLESHOOTING_FILE=$MAIN_DIRECTORY/troubleshooting.md

CONTENTS_FILE=$CUR_DIRECTORY/contents.md
STRUCTURE_FILE=$CUR_DIRECTORY/sections/project_structure.md

declare -a contents=(
    $CUR_DIRECTORY/contents
    $CUR_DIRECTORY/sections/start
    $CUR_DIRECTORY/sections/browser_support
    $CUR_DIRECTORY/sections/project_structure
    $CUR_DIRECTORY/sections/acknowledgments
    $CUR_DIRECTORY/sections/license
)

declare -a index_contents=(
    $CUR_DIRECTORY/contents
    $CUR_DIRECTORY/sections/start
)

function write_to() {
    cat "${2}.md" >>$1
    printf "\n" >>$1
}

# Converts from pascal case to dash case
function convert_to_internal_link() {
    echo $1
    result=$(echo $1 |
        sed 's/\(.\)\([A-Z]\)/\1-\2/g' |
        tr '[:upper:]' '[:lower:]')
    return $result
}

function write_to_contents() {
    title=$(head -n 1 ${1}.md | cut -c3- | xargs)
    converted_title=$(
        echo $title |
            sed 's/\(.\)\([A-Z]\)/\1-\2/g' |
            tr '[:upper:]' '[:lower:]' |
            sed 's/ //g'
    )
    echo "- [$title](#$converted_title)" >>$CONTENTS_FILE
}

function reset_all() {
    printf "" >$README_FILE
    printf "" >$TROUBLESHOOTING_FILE
}

function adjust_image_location_reference() {
    if [[ "$OSTYPE" =~ "darwin"* ]]; then # macOS
        sed -i '' -e 's+../images/+./docs/images/+g' $1
    else
        sed -i '' 's+../images/+./docs/images/+g' ${1}
    fi
}

reset_all

# README
function make_readme() {
    # Project structure file
    echo "# Project Structure" >$STRUCTURE_FILE
    echo "" >>$STRUCTURE_FILE
    echo "\`\`\`" >>$STRUCTURE_FILE
    tree -I 'dist' >>$STRUCTURE_FILE 2>&1
    if [[ "$OSTYPE" =~ "darwin"* ]]; then # macOS
        sed -i '' -e '$ d' $STRUCTURE_FILE
    else
        sed -i '$ d' $STRUCTURE_FILE
    fi
    echo "\`\`\`" >>$STRUCTURE_FILE

    # Put onto contents page
    echo "## Table Of Contents" >$CONTENTS_FILE
    echo "" >>$CONTENTS_FILE

    # Write to contents file first
    for contents_file in "${contents[@]}"; do
        write_to_contents $contents_file
    done

    # Write sections
    # cat $CUR_DIRECTORY/logo.txt >>$README_FILE
    # printf "\n" >>$README_FILE
    write_to $README_FILE $CUR_DIRECTORY/sections/introduction
    for contents_file in "${contents[@]}"; do
        write_to $README_FILE $contents_file
    done
    adjust_image_location_reference $README_FILE
}

# INDE_FILE

function make_index() {
    write_to $INDEX_FILE intro
}

# TROUBLESHOOTING
function make_troubleshooting() {
    printf " # Troubleshooting \n" >$TROUBLESHOOTING_FILE
    # printf "\`\`\\n" >> $TROUBLESHOOTING_FILE

    write_to $TROUBLESHOOTING_FILE $CUR_DIRECTORY/sections/troubleshooting

    printf "# Git todo's \n" >>$TROUBLESHOOTING_FILE
    # printf "\`\`\`\n" >>$TROUBLESHOOTING_FILE
    # $(printf "$(cd .. && git grep -l TODO | xargs -n1 git blame -f -n -w | grep "Your name" | grep TODO | sed "s/.\{9\}//" | sed "s/(.*)[[:space:]]*//")") >>$TROUBLESHOOTING_FILE
    # printf "\`\`\`\n" >>$TROUBLESHOOTING_FILE
    adjust_image_location_reference $TROUBLESHOOTING_FILE
}

make_readme
# make_index
# make_troubleshooting
