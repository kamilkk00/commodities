FUNC ?= func
APP ?= 

.PHONY: start deploy

start:
	$(FUNC) start

deploy:
	$(FUNC) azure functionapp publish $(APP) --incremental