#!/bin/bash

echo "What's the version number?"
read VERSION

# publish master branch
git commit -am "v$VERSION"

echo "Add a comment?"
read comment

if [[ $comment ]]; then
	git tag -a v$VERSION -m "$comment" -f
else
	git tag v$VERSION -f
fi
	
git push --tags -f
git push