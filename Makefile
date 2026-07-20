NPM := npm

.PHONY: web
web: web-deps web-build

.PHONY: web-build
web-build:
	cd web && $(NPM) run build

.PHONY: web-deps
web-deps:
	cd web && $(NPM) ci
