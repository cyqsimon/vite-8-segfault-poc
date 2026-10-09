NPM := npm

.PHONY: web
web: web-deps web-build

.PHONY: web-build
web-build:
	cd web && ./build.mjs

.PHONY: web-deps
web-deps:
	cd web && $(NPM) ci
