.PHONY: test
test:
	pytest -vv

.PHONY: clean
clean:
	@echo "Cleaning up Python cache files..."
	# Find and remove all __pycache__ directories and .pyc files.
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	rm -rf .pytest_cache
	@echo "Cleanup complete."
