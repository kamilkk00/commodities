FUNC ?= func
APP ?= $(FUNCTION_NAME)

.PHONY: start deploy

start:
	$(FUNC) start

deploy:
	$(FUNC) azure functionapp publish $(APP) --incremental

info: 
	$(FUNC) azure functionapp list-functions $(APP) --show-keys