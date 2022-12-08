#################################################################################
# COMMANDS                                                                      #
#################################################################################
.PHONY: docs-%
## Build documentation in the format specified after `-`
## (e.g.,
## `make docs-html` builds the docs in HTML format,
## `make docs-confluence` builds and publishes the docs on confluence (see `docs/source/conf.py` for details),
## `make docs-clean` cleans the docs build directory)
docs-%: LAUNCH_DOCS_PREVIEW ?= true
docs-%:
	$(MAKE) $* LAUNCH_DOCS_PREVIEW=$(LAUNCH_DOCS_PREVIEW) -C docs

.PHONY: test-docs
## Test documentation format/syntax
test-docs:
	poetry run tox -e docs
