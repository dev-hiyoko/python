.PHONY: init
init: git/commit-template
	pip install -r requirements.txt

# git
.PHONY: git/commit-template
git/commit-template:
	git config commit.template ./.github/.gitmessage.txt &&\
	git config --add commit.cleanup strip
