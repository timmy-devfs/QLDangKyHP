.PHONY: up down build logs clean ps help
up:
	docker-compose up -d
down:
	docker-compose down
build:
	docker-compose build --no-cache
logs:
	docker-compose logs -f
clean:
	docker-compose down -v --remove-orphans
ps:
	docker-compose ps
help:
	@echo.
	@echo   BICAP System - Available Commands:
	@echo   make up      - Start all infrastructure
	@echo   make down    - Stop all containers
	@echo   make build   - Rebuild images
	@echo   make logs    - View realtime logs
	@echo   make clean   - Remove all containers + volumes
	@echo   make ps      - Show container status
	@echo.