COMPOSE := docker compose

VOLUMES := $(shell docker volume ls -q)

build: 
	$(COMPOSE) up --build

down:
	$(COMPOSE) down -v

clean: down
	docker system prune -f -a --volumes

re: clean
	$(MAKE) build

revolume: down
	if [ -n "$(VOLUMES)" ]; then docker volume rm -f $(VOLUMES); fi
	$(MAKE) build

.PHONY: build down clean re revolume